



from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
generated_images = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    #image generation logic
    generated_image = generate_image(data)
    generated_images.append(generated_image)
    return jsonify({'success': True})
  
@app.route('/images')
def get_images():
    return jsonify(generated_images)
  
if __name__ == '__main__':
    app.run()



