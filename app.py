import os
import importlib.metadata
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()

# 檢查 groq 套件版本
try:
    groq_version = importlib.metadata.version('groq')
    print(f"已安裝 groq 套件版本: {groq_version}")
except importlib.metadata.PackageNotFoundError:
    groq_version = None
    print("未安裝 groq 套件")

# 導入 Groq 套件
try:
    from groq import Groq
except ImportError:
    os.system('pip install groq')
    from groq import Groq

app = Flask(__name__)

# 設定 Groq API 金鑰
GROQ_API_KEY = "YOUR GROQ API KEY"


# 系統提示詞
def get_system_prompt():
    """從檔案讀取系統提示詞"""
    import os
    try:
        # 使用絕對路徑找到檔案
        base_dir = os.path.dirname(os.path.abspath(__file__))
        prompt_file = os.path.join(base_dir, 'system_prompt_easy.txt')
        with open(prompt_file, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"讀取系統提示詞檔案時發生錯誤: {e}")
        return "你是 NexusTech 公司的智能客服助手。"

SYSTEM_PROMPT = get_system_prompt()

@app.route('/')
def index():
    return render_template('index.html')

def chat(user_message):
    """使用 Groq API 處理聊天請求"""
    # 系統提示詞
    system_prompt = {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
    
    # 準備消息列表
    messages = [system_prompt, {"role": "user", "content": user_message}]
    
    try:
        print(f"建立 Groq API 客戶端...")
        # 以符合 hugging face 的方式初始化 Groq 客戶端
        client = Groq(api_key=GROQ_API_KEY)
        
        print(f"向 Groq API 發送請求...")
        completion = client.chat.completions.create(
            model="llama3-70b-8192",  # 使用 Llama 3 70B 模型
            messages=messages,
            temperature=0.7,
            max_tokens=1024,
            top_p=1,
            stream=False,
            stop=None,
        )
        
        # 獲取回應內容
        response = completion.choices[0].message.content
        print(f"成功從 Groq API 取得回應")
        return response
        
    except Exception as e:
        error_msg = str(e)
        print(f"請求 Groq API 時發生錯誤: {error_msg}")
        return f"API 請求錯誤: {error_msg}"

@app.route('/api/chat', methods=['POST'])
def handle_chat_request():
    """
    處理聊天請求並確保始終返回 JSON 格式回應
    """
    try:
        # 從請求中獲取 JSON 數據
        data = request.get_json()
        if not data:
            print("錯誤: 請求資料格式不正確")
            return jsonify({"error": "請求資料格式不正確"}), 400
            
        # 獲取用戶訊息
        user_message = data.get('message', '')
        if not user_message.strip():
            print("錯誤: 空白訊息")
            return jsonify({"error": "請提供訊息內容"}), 400
            
        # 調用 chat 函數獲取回應
        print(f"收到聊天請求: '{user_message}'")
        response_text = chat(user_message)
        print(f"回應長度: {len(response_text)} 字符")
        
        # 返回 JSON 格式的響應
        response = jsonify({"response": response_text})
        response.headers.add('Content-Type', 'application/json')
        return response
    
    except Exception as e:
        import traceback
        error_msg = str(e)
        traceback_str = traceback.format_exc()
        print(f"錯誤: {error_msg}")
        print(f"堆疊追踪: {traceback_str}")
        return jsonify({"error": f"API 請求錯誤: {error_msg}"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
