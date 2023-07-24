# 🦙💬 Llama 2 Chat

This chatbot is created using the open-source Llama 2 LLM model from Meta.

Particularly, we're using the [**Llama2-7B**](https://replicate.com/a16z-infra/llama7b-v2-chat) model deployed by the Andreessen Horowitz (a16z) team and hosted on the [Replicate](https://replicate.com/) platform.

This app was refactored from [a16z's implementation](https://github.com/a16z-infra/llama2-chatbot) of their [LLaMA2 Chatbot](https://www.llama2.ai/) to be light-weight for deployment to the [Streamlit Community Cloud](https://streamlit.io/cloud).

## Demo App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://llama2.streamlitapp.com/)

## Prerequisite libraries

```
streamlit
replicate
```

## Getting your own Replicate API token

To use this app, you'll need to get your own [Replicate](https://replicate.com/) API token.

After signing up to Replicate, you can access your API token from [this page](https://replicate.com/account/api-tokens).

## Other Llama 2 models to try

As mentioned above, this chatbot implementation uses the [**Llama2-7B**](https://replicate.com/a16z-infra/llama7b-v2-chat) model that was trained on 7 billion parameters.

You can also try out the larger models:
- [Llama2-13B](https://replicate.com/a16z-infra/llama13b-v2-chat)
- [Llama2-70B](https://replicate.com/replicate/llama70b-v2-chat)

## Further Reading
- [Llama 2 website](https://ai.meta.com/llama/)
- [Llama 2 technical overview](https://ai.meta.com/resources/models-and-libraries/llama/)
- [Llama 2 blog](https://ai.meta.com/blog/llama-2/)
- [Llama 2 research article](https://ai.meta.com/research/publications/llama-2-open-foundation-and-fine-tuned-chat-models/)
- [Llama 2 GitHub repo](https://github.com/facebookresearch/llama/tree/main)
