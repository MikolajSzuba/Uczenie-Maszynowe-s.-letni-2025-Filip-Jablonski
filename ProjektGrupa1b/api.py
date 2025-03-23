from google import genai

def read_credentials(path):
    """
    Reads credentials for Gemini API from file (API key)
    Args:
        path: path to file containing API key
    Returns:
        String: API key
    """
    with open(path, 'r') as f:
        lines = f.readlines()
    return lines[0].strip()

def send_prompt(api_key, prompt):
    """
    Sends prompt to Gemini API
    Args:
        api_key: API key
        prompt: prompt to send to Gemini API
    Returns:
        String: response from Gemini
    """
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )
    return response


if __name__ == '__main__':
    api_key = read_credentials('credentials.txt')
    prompt = "Generate a script for short video about cats"

    response = send_prompt(api_key, prompt)
    print(response.text)
