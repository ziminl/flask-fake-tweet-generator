



import base64
from PIL import Image
from io import BytesIO

def generate_image(data):
    image_size = data.get('size')
    image_color = data.get('color')
    image = Image.new('RGB', image_size, image_color)
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    encoded_image = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return encoded_image

##put ur missing one

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    generated_image = generate_image(data)
    generated_images.append(generated_image)
    return jsonify({'success': True})
