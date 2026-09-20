<!-- 1405-06-29 -->

### Installation:
- pip install -U langchain
- uv add langchain # OR
- pip install -qU langchain "langchain[anthropic]" # q: quietly

### Check Installation
- python -c "import langchain; print(langchain.__version__)" 

### Integration:
- pip install -U langchain-deepseek
- pip install -U langchain-anthropic
- pip install -U langchain-openai
- python -c "import anthropic; print(anthropic.__version__)"

### Set and Run:
- set DEEPSEEK_API_KEY=XXX # in cmd
- python basic.py
