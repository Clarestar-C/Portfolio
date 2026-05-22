import os
from openai import OpenAI

# Initialize the NVIDIA client
client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "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"
)

print("--- 🚀 Requesting Premium Design from Llama 4 Maverick ---")

# Define the detailed prompt
prompt = (
    "Create a high-end, one-page portfolio for an Electrical Engineering student named Claresta at McMaster. "
    "DESIGN RULES: "
    "1. Use a deep 'Midnight' background (#0a0a0c) with glowing neon blue and slate accents. "
    "2. Use 'Glassmorphism' for the project cards (semi-transparent with background-blur). "
    "3. Replace broken images with stylish 'SVG Icons' (e.g., a CPU icon for microcontrollers). "
    "4. Include a 'Hero Section' with a glowing gradient text effect. "
    "5. Add a grid for skills like Python, C, and PCB Design using borders that glow on hover. "
    "6. Make sure the 'MSP432 Microcontroller LED Flasher' and 'DC Power Supply Design' projects look like premium feature cards. "
    "IMPORTANT: Return ONLY the raw HTML/CSS code. Do not include any conversational text before or after the code."
)

try:
    completion = client.chat.completions.create(
      model="meta/llama-4-maverick-17b-128e-instruct",
      messages=[{"role":"user","content": prompt}],
      temperature=0.2,
      top_p=0.7,
      max_tokens=4096, # Increased to ensure the full site is generated
      stream=True
    )

    full_code = ""
    print("Writing code to terminal and index.html...")

    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            print(content, end="") # See it happening live
            full_code += content
    
    # Clean up the output: Remove markdown code blocks if the AI included them
    clean_code = full_code.replace("```html", "").replace("```", "").strip()

    # Automatically save to index.html
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(clean_code)
    
    print("\n\n✅ SUCCESS: index.html has been updated with the new design!")
    print("Refresh your browser to see the changes.")
        
except Exception as e:
    print(f"\n❌ Error: {e}")