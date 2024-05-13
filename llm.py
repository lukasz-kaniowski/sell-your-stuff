import base64
import anthropic

client = anthropic.Anthropic()

prompt = """Describe the image as if you were selling it on an online marketplace.
Include the item's condition, size, color, and any other relevant details.
Format your response with title, description and bullet point specification.
Title should contain the brand name.
""".strip()


def get_item_description(image):
    img1_base64 = base64.b64encode(image.read()).decode("utf-8")
    message = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1272,
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": image.type,
                            "data": img1_base64
                        }
                    },
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ]
    )

    return message.content[0].text
