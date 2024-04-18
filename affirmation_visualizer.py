 # Set your OpenAI API key as an environment variable
import os
import openai
from openai import OpenAI
import time
def affirmation_visualizer(transcript, folder_name, key):
    
    print(transcript)
    class ChatCompletionMessage:
        def __init__(self, content, role, function_call=None, tool_calls=None):
            self.content = content
            self.role = role
            self.function_call = function_call
            self.tool_calls = tool_calls

        def get_text_content(self):
            # Return only the text content
            return self.content
        # Initialize the OpenAI client
    client = openai.OpenAI(api_key=key)

    # Your code for interacting with the OpenAI API goes here
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "your job is to translate general affirmations into examples of SPECIFIC (use specific parts of the general area, like if it says argument you show yell, scream, cry, hug, break, etc instead of bicker, dispute, embrace, decompose, and all those abstract words) physical , visual, concrete, not-up-for-interpretation, robot-parseable, physical-words-only situations which imply that those general beliefs are in the person’s mind. you will never actually output anything general or vague, there should always be an answer to who what where. if two people were to draw this their drawing should be exactly the same, the exact same physical solution because it’s not up for debate or interpretation what the prompt means. Sentences generated should be in third-person perspective, usually it is assumed a woman. please be very creative with thiss so that it is not generic, we don't want the uther tb bored by looking at just an everyday action, we want the user to feel comforted by the clear and vivid positive emotions that is shown in the image (again, using specific physical descriptions of specific physical situations, not vague or abstract, to get across the positivity). if the prompt is a relationship, a bad output would be 7 outputs of generic couple together. a good output would be outputs with a woman getting hugged, a woman cuddling in bed with her man, a woman opening up a cute love letter, a woman seeing her man get on one knee with a ring, a woman seeing her man bring her food, a man handing a woman money, a woman looking at a painting of herself with a heart on it that says 'love boyfriend'. do not use any quotes in your response as that will mess up the code, put any quotes in parenthesis. see how much better and distinct each one is. And please generate one python command for each affirmation (you'll see the python format to follow at the end of this). please make each physical situation very unique, very specific, and highly relevant to the affirmation (so if someone is releasing negative attachment, we should see them sighing in relief or smiling gently as they walk away from their computer knowing they dont need to do the thing anymore, etc.) very specialized and specific situations tailored to the affirmation. please dont have them look like each other -- each scene you generate should be distinct, different from the rest you generate. be creative with it. make sure you generate one python command for each affirmation--that is, you must have a minimum of 7 commands as your output. if you have her interacting with things (like a run button or a book), describe the object. 'a rectangular run button appears on the screen visible to the camera', 'a spherical orange basketball with black lines comes towards the camera', etc. relative camera position on objects. always describe a positive or neutral expression on the person explicitly. also please use the word 'photorealistic'. be very creative with this; i want very varied scnees, each one very different from the one before. also, be very explicit--the ai interpreting this doesnt knoow what an online banking app is, so you have to say 'green circle with $ dollar sign and ! exclamantion ppoint' for example if you wanted to describ ea banking app. have to describe everything like youre explaining it to an alien almost, very thorough detailed. please also keep in mind that your code is going to be passed as raw code so please do not include anything other than raw code in your prompts. now generate one scene for each prompt (and refer to white people as white caucasian light-skinned in it), and please generate one image per affirmation, and please instead of using words like 'her face is serene' say 'her lips have a gentle smile and her eyes look happy, and her body language is open because her shoulders are rounded back in her chair and she's sitting up tall puffing her chest out' describing nationality as American ('photorealistic caucasian light-skinned white American' for white). Please also use creative imagery: if you want to describe someone being calm as they do a task, don't just have prompts where they're doing the task in a bland way. Get creative; have them meditating with a poster of the subject behind them for example, or have them give a thumbs up and smile to an object of the task, or show them high fiving someone with a T-shirt that has an object of the task, etc. always use the word photorealistic in each prompt. also, please do not tell the AI to write images with text on it because it is bad with text. and make sure your output is exactly this form with no numeration or bullet pts. If you separate your python commands by ANYTHING other than a new line, the code will break. keep in mind you cannot use quote marks in your response, and keep in mind that the visualizing AI parses each word as an image input (so saying popping each bubble'interprets popping,each,bubble as image keywords), so it is actually better to say popped bubble and generally use short participle-adjective noun combinations like that as opposed to subject verbs the object. Keep in mind that if a tangible thing is used as an object in a sentence (like she looks at the screen), the object (in this case the screen) will often not be parsed so you have to instead say woman facing black computer screen with green checkmark visible or something else descriptive like that. use words like 'reject' instead of 'say no' and generally avoid compound/unimageable words if you can. and also use this format: python -m stability_sdk generate <prompt> --width 900 --height 520"},
           {"role": "user", "content": str(transcript)}
        ]
    )


    # Extract the actual content generated by GPT-3.5 Turbo
    generated_message = completion.choices[0].message
    generated_message_object = ChatCompletionMessage(
        content=generated_message.content,
        role='assistant'  # Assuming the role is 'assistant'
    )

    # Print out the text that will be read
    visualizations = generated_message_object.get_text_content()
    # Save the text content to a file
    with open('output_text_visual.txt', 'w') as file:
        file.write(visualizations)
    print('Done with visualization prompts')
    return visualizations
  