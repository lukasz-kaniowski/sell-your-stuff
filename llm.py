import base64
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage

chat = ChatAnthropic(model="claude-3-haiku-20240307")

prompt = """Describe the image as if you were selling it on an online marketplace.
Include the item's condition, size, color, and any other relevant details.
Format your response with title, description and bullet point specification.
Title should contain the brand name.
""".strip()


def get_item_description(image):
    # img1_base64 = base64.b64encode(img1_path.read_bytes()).decode("utf-8")
    img1_base64 = base64.b64encode(image.read()).decode("utf-8")
    print(image)
    messages = [
        HumanMessage(
            content=[
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:{image.type};base64,{img1_base64}",
                    },
                },
                {
                    "type": "text",
                    "text": prompt
                },
            ]
        )
    ]
    return chat.invoke(messages).content
