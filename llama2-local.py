from llama_cpp import Llama 
import timeit

# Load Llama 2 model
llm = Llama(model_path="llama-2-7b-chat.ggmlv3.q2_K.bin",
            n_ctx=512,
            n_batch=128)

# Start timer
start = timeit.default_timer()

# Generate LLM response
prompt = "What is Python?"

output = llm(prompt,
             max_tokens=-1,
             echo=False,
             temperature=0.1,
             top_p=0.9)

# Stop timer
stop = timeit.default_timer()
duration = stop - start
print("Time: ", duration, '\n\n')

# Display generated text
print(output['choices'][0]['text'])

# Write to file
with open("response.txt", "a") as f:
  f.write(f"Time: {duration}")
  f.write(output['choices'][0]['text'])
