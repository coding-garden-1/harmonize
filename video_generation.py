import requests

response = requests.post(
    f"https://api.stability.ai/v2alpha/generation/image-to-video",
    headers={"authorization": f"Bearer sk-3G2XCkYoceBdSG9sN0PWnmkyN9VabSB9x2gU5Syz2MxkA7q8"},
    files={"image": open("./kittens-in-space.png", "rb")},
    data={
        "seed": 0,
        "cfg_scale": 1.8,
        "motion_bucket_id": 127
    },
)

if response.status_code == 200:
    try:
        generation_id = response.json().get('id')
        print("Generation ID:", generation_id)
    except requests.exceptions.JSONDecodeError:
        print("Error: Unable to decode JSON in the response.")
else:
    print(f"Error: {response.status_code} - {response.text}")
