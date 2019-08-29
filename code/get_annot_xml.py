import os
import urllib
import json
import pandas as pd
import xml.etree.cElementTree as ET

file = './data/indian_number_plates.json'
df = pd.read_json(file, lines=True)

df.dropna(subset=['annotation'], inplace=True)

annot = df['annotation'].values
annot = [x[0] for x in annot]

urls = df['content'].values

for i,a in enumerate(annot):

	w = a['imageWidth']
	h = a['imageHeight']

	root = ET.Element('annotation')
	filename = ET.SubElement(root, 'filename').text = '{}.jpg'.format(i)
	size = ET.SubElement(root, 'size')
	ET.SubElement(size, "width").text = str(int(w))
	ET.SubElement(size, "height").text = str(int(h))
	obj = ET.SubElement(root, 'object')
	ET.SubElement(obj, 'name').text = a['label'][0]
	bndbox = ET.SubElement(obj, 'bndbox')
	ET.SubElement(bndbox, 'xmin').text = str(int(a['points'][0]['x'] * w))
	ET.SubElement(bndbox, 'ymin').text = str(int(a['points'][0]['y'] * h))
	ET.SubElement(bndbox, 'xmax').text = str(int(a['points'][1]['x'] * w))
	ET.SubElement(bndbox, 'ymax').text = str(int(a['points'][1]['y'] * h))

	tree = ET.ElementTree(root)

	if not os.path.exists('./annotations/xmls'):
		os.makedirs('./annotations/xmls')

	file = './annotations/xmls/{}.xml'.format(i)
	with open(file, 'wb') as f:	
		tree.write(f, encoding='utf-8')

	# if not os.path.exists('./images'):
	# 	os.makedirs('./images')

	# urllib.urlretrieve(urls[i], './images/{}.jpg'.format(i))