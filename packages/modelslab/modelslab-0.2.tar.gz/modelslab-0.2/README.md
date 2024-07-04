<<<<<<< HEAD
## ModelsLab API Package

This package provides a convenient way to interact with the ModelsLab API, allowing you to generate images from text prompts using state-of-the-art deep learning models.
=======
## ModelsLab API Python Package

This Python Package provides a convenient way to interact with the ModelsLab API, allowing you to generate images from text prompts using state-of-the-art deep learning models.
>>>>>>> 3a32d04ecbee63db344d85a0533c561d80777832

### Installation

To install the ModelsLab API package, simply use pip:

`pip install modelslab`

Usage

To use the package, follow these steps:

1. Import the `ModelsLab` instance into your project

`from modelslab import ModelsLab` 

2. Obtain an API key from ModelsLab. If you don't have an API key yet, please [subscribe](https://modelslab.com/pricing) to their products and copy the api key from your [dashboard](https://modelslab.com/dashboard/apikey)

Modelslab has many API endpoint categories depending on your need. For instance, let interact with the Image Editing endpoint

```
from modelslab import ModelsLab

modelslab = ModelsLab()

response = modelslab.image_editing.super_resolution(
    key="YOUR_API_KEY",
    image_url ="url of the image"
)

print(response)

```


Replace `YOUR_API_KEY` with the actual API key provided to you by ModelsLab.


### Notes

- The ModelsLab API currently supports real-time text-to-image generation. Additional features and capabilities may be added in the future.
- Ensure that you have a valid API key before using the package. If you encounter any issues with your API key, please contact ModelsLab for assistance.
- Be mindful of the usage limits and terms of service associated with your API key.

### Support

If you have any questions, issues, or feedback regarding the ModelsLab API package, please reach out to the ModelsLab support team at support@modelslab.com.

<<<<<<< HEAD
Happy image generation!
=======
Happy image generation!
>>>>>>> 3a32d04ecbee63db344d85a0533c561d80777832
