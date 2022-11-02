from pycaret.classification import *
def forcast(data):
    saved_final_lr = load_model('Final_LR_Model')
    new_prediction = predict_model(saved_final_lr, data=data)
    return new_prediction