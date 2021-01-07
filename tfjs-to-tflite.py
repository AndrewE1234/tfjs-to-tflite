# tflite-converter
# Andrew Eljumaily 2021
#
# A tfjs-layers to tflite converter

import sys
import os

if len(sys.argv) <= 1:
  sys.exit("ERROR: Must include path to input file as argument.\nEX: python {} models/model.json".format(sys.argv[0]))

fileName = sys.argv[1]
if fileName == "-h" or fileName == "--help":
  print("tflite-converter, Andrew Eljumaily 2021\nA simple to use tfjs-layers to tflite converter\n\n Usage: {} <path/to/input/file.json>\n Output will save to /converted/model.tflite".format(sys.argv[0]))
  sys.exit()

# Convert a tfjs layers file to a keras file using tensorflowjs_converter (part of tesnorflowjs)
os.system("tensorflowjs_converter --input_format=tfjs_layers_model --output_format=keras {} converted/saved_model.h5".format(fileName))

import tensorflow as tf

# Load a model using high-level tf.keras.* APIs
model = tf.keras.models.load_model('converted/saved_model.h5')

# Convert the model.
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the model.
with open('/converted/model.tflite', 'wb') as f:
  f.write(tflite_model)

os.remove("converted/saved_model.h5")

print("Conversion complete!")
