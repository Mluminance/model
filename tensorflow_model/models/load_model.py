json_file = open('models/DA_dnn.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
 
loaded_model.load_weights('models/DA_dnn.h5'))