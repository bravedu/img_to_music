import services.imgToMusic
from flask import Flask, request, jsonify

aa = services.imgToMusic.imgtextToMpt("painting of a landscape with a river and a house in the distance")

print(aa)