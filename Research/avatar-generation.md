# Avatar Generation

## Prompt that will be used:
frontal portrait of a **PLACEHOLDER**, midshot intensity, white studio background, white background, relaxed mimic, photo taken with provia --ar 2:3 --style raw

- the value of **PLACEHOLDER** will be determined by the user
- he can choose the gender, skin- and hair color, whether the person should wear glasses and my more

## DALL-E
https://arxiv.org/abs/2003.07405

- developed by OpenAI
- groundbreaking model that is capable of generating highly creative and novel images from textual descriptions
- Can generate images of objects and concepts that do not exist in the real world
- But generating high-resolution images can be challenging for this model
- DALL-E may generate images that exhibit biases present in the training data
- Using this model would have been optimal because it uses the same API Key as the Text-to-Text task
- user would not need to create another account on another platform
- but there is a limited amount of calls to the api that can be made (for free)
- you need a phone number linked to your account to use OpenAI -> prevents you for being able to generate as many new account with free credits as you want
- Dall-E was not optimal for the task of generating an avatar of an almost real person.
- I had the requirements of getting frontal midshot pictures of humans
- Either the quality of the picture was not good or the human looked painted or somehow animated or in the worst case the human looked like he was ill

## DreamStudio
https://platform.stability.ai/docs/features
- developed by stability.ai
- easy to use and well documented
- capable of generating images from textual description in multiple styles, for example digital art, anime, enhanced pictures, comic book style and many more
- you can set many options that influence how the images will look like. 
    - generation steps: how many times the image is sampled
    - seed: allows to reproduce the same image when giving the model the same prompt and options
    - Prompt strength: determines how much the final image will portray your prompt
    - model: able to choose betweeen multiple models with each having its own strengths (for example whether the images should look more creative or realistic and so on)
    - negative prompt: you are able to provide the model with information you want to avoid
- The images of this model look very promising
- Humans are very realistic and nearly every picture comes out in a frontal midshot view
- Advantages to DALL-E:
    - you can create as many new accounts with free credits as you want because there is no phone number linked to your account
    - better documentation and easier to use than dall-E
    - the template code that is available in the documentation is a great starting point to use the API
    - you can try out the different models and styles and every option is given as a comment in the code which means you do not need to search them
- the only package that needs to be installed is the stability-sdk
- picture generation is very fast

