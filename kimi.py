@'
import sys
import requests
import json
from datetime import datetime

# ===================== CONFIGURAÇÃO MOONSHOT =====================
MOONSHOT_API_KEY = "sk-Zjhg6YlBv0FyoYsao9F0jOdl5JrcxkxQSXOzQ1Axofbkv47Q"
MODEL = "kimi-k2-thinking"
API_ENDPOINT = "https://api.moonshot.ai/v1"
# ===============================================================

class KimiChat:
    def __init__(self):
        self.history = []
        self.total_tokens = 0
        
    def chamar_api(self, messages):
        """Chama API Moonshot com histórico"""
        try:
            response = requests.post(
                f"{API_ENDPOINT}/chat/completions",
                headers={
                    "Authorization": f"Bearer {MOONSHOT_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": MODEL,
                    "messages": messages,
                    "stream": False
                },
                timeout=60
            )
            
            if response.status_code != 200:
                print(f"\n❌ ERRO {response.status_code}", file=sys.stderr)
                print(response.text, file=sys.stderr)
                return None
                
            data = response.json()
            self.total_tokens += data.get("usage", {}).get("total_tokens", 0)
            return data["choices"][0]["message"]["content"]
            
        except Exception as e:
            print(f"\n❌ Erro: {e}", file=sys.stderr)
            return None
    
    def ler_arquivos(self, prompt):
        """Lê arquivos mencionados (@arquivo.py)"""
        import re
        arquivos = re.findall(r'@(\S+)', prompt)
        for arquivo in arquivos:
            try:
                with open(arquivo, 'r', encoding='utf-8') as f:
                    conteudo = f.read()
                    prompt = prompt.replace(f"@{arquivo}", f"Arquivo `{arquivo}`:\n```\n{conteudo}\n```\n")
            except:
                print(f"⚠️ Não consegui ler {arquivo}")
        return prompt
    
    def modo_interativo(self):
        """Chat contínuo igual Gemini CLI"""
        print("🚀 Kimi K2 CLI - Modo Interativo")
        print("💡 Dicas: /clear (limpar), /quit (sair), @arquivo.py (contexto)")
        print("=" * 50)
        
        while True:
            try:
                # Pergunta ao usuário
                pergunta = input("\nVocê: ").strip()
                
                if not pergunta:
                    continue
                    
                # Comandos especiais
                if pergunta.lower() == "/quit":
                    print("👋 Até logo!")
                    break
                elif pergunta.lower() == "/clear":
                    self.history = []
                    print("🗑️ Histórico limpo!")
                    continue
                elif pergunta.lower() == "/help":
                    print("Comandos: /quit, /clear, @arquivo.py")
                    continue
                
                # Lê arquivos se mencionados
                pergunta = self.ler_arquivos(pergunta)
                
                # Adiciona ao histórico
                self.history.append({"role": "user", "content": pergunta})
                
                # Chama API (mantém apenas últimas 10 mensagens para não extrapolar token)
                messages = self.history[-10:]
                print("\nKimi: ", end="", flush=True)
                
                resposta = self.chamar_api(messages)
                if resposta:
                    print(resposta)
                    self.history.append({"role": "assistant", "content": resposta})
                else:
                    print("❌ Falha na resposta")
                    
            except KeyboardInterrupt:
                print("\n\n👋 Até logo!")
                break
            except EOFError:
                print("\n\n👋 Até logo!")
                break
    
    def modo_inline(self, prompt):
        """Um comando só, igual ao script anterior"""
        prompt = self.ler_arquivos(prompt)
        messages = [{"role": "user", "content": prompt}]
        
        resposta = self.chamar_api(messages)
        if resposta:
            print(resposta)
            return True
        return False

def main():
    chat = KimiChat()
    
    # Se tem argumentos, modo inline
    if len(sys.argv) > 1:
        prompt = " ".join(sys.argv[1:])
        sucesso = chat.modo_inline(prompt)
        sys.exit(0 if sucesso else 1)
    
    # Se não tem argumentos, modo interativo
    chat.modo_interativo()

if __name__ == "__main__":
    main()
'@ | Out-File -FilePath kimi.py -Encoding utf8 -NoNewline