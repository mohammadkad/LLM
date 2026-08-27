<!-- 1405-06-03 -->

## Definitions:
- Agent = Model + Harness
  - The harness is everything around the model loop: the prompt, the tools, and any middleware that shapes behavior.

## AI coding:
### IDE & Harness:
- deepseek harness
  - npx @deepseek-ai/dsh web
  - http://127.0.0.1:3080

- opencode: https://opencode.ai
- Claude Code: https://github.com/anthropics/claude-code
  - irm https://claude.ai/install.ps1 | iex
  - claude --version

- Claude code:
  - Before login > Help > Troubleshooting > Enable Developer Mode
  - Developer > Configure Third-party inference

### Routers:
- openrouter.ai
- https://9router.com
  - npm install -g 9router
  - 9router
  - http://localhost:20128/dashboard
    - Add providers: Anthropic Compatible or OpenAI Compatible
    - Add Connection
    - use : http://localhost:20128/v1 + API Keys

- https://omniroute.online
  - npm install -g omniroute
  - omniroute
  - curl localhost:20128/v1/models

### Fa:
- avalai.ir
  - https://api.avalai.ir/v1

### Models:
- https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash

### Tools
- codegraph: https://github.com/colbymchenry/codegraph
  - irm https://raw.githubusercontent.com/colbymchenry/codegraph/main/install.ps1 | iex
  - codegraph --version
  - codegraph install
  - cd your-project + codegraph init
