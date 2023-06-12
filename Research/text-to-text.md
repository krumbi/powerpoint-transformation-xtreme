# text-to-text Component

## Text extraction

### PDF-Reader

- This [library](https://github.com/py-pdf/pypdf) seems very suitable for this task as it supports reading PDFs compared to other libraries for Python which focus on creating or editing PDFs

### PowerPoint

- https://github.com/scanny/python-pptx

## Text-to-Text ML model

### Example prompt

Can you write me a summary of the following text for a presentation?

```
First, a quick review…

- web page consists of objects, each of which can be stored on different Web servers

- object can be HTML file, JPEG image, Java applet, audio file,…

- web page consists of base HTML-file which includes several referenced objects, each adressable by a URL, e.g.,
```

### ChatGPT

- supports Chat Markup Language

- API has costs

#### Result

In a web page, various objects such as HTML files, JPEG images, Java applets, and audio files are stored on different web servers. These objects are referenced and included in a base HTML file, which serves as the foundation of the web page. Each object is uniquely addressable through a URL (Uniform Resource Locator), allowing users to access and view the content seamlessly.

### LLaMA

- 65-billion-parameter

- Access has to be requested

- has to be run locally with powerful GPU

### Stanford Alpaca

- model not publically available

- fine tuned from LLaMA

- can be accessed with [this](https://huggingface.co/spaces/tloen/alpaca-lora) through websockets

#### Result

A web page consists of objects, each of which can be stored on different Web servers. An object can be an HTML file, a JPEG image, a Java applet, an audio file, etc. A web page consists of a base HTML-file which includes several referenced objects, each of which can be accessed by a URL.

### Vicuna

- fine tuned from LLaMA

- has to be run locally with powerful GPU

### DeepAI text generator

- based on GPT-2

- API available, 5$ per 100 API calls

#### Result

A web page is made up of various objects, such as HTML files, images, applets, and audio files, which can be stored on different servers. The page itself consists of a base HTML file and may include several other objects.
