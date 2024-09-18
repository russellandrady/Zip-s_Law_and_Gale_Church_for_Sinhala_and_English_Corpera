import json
import numpy as np

def calculate_fx_r_stability(word_data, output_data):
    output_dict = {}
    for entry in output_data:
        for word in entry['Words']:
            output_dict[word] = entry
    
    fxr_products = []
    
    for word, freq in word_data.items():
        if word in output_dict:
            rank = output_dict[word]['Rank']
            count = output_dict[word]['Count']
            fxr_product = rank * count
            
            fxr_products.append(fxr_product)
    
    return fxr_products

def compute_statistics(fxr_products, language):
    mean_fxr = np.mean(fxr_products)
    std_fxr = np.std(fxr_products)
    print(f'Statistical Analysis for {language} corpus:')
    print(f'Mean f * r: {mean_fxr:.2f}')
    print(f'Standard Deviation of f * r: {std_fxr:.2f}')
    print('---' * 10)
    
    return mean_fxr, std_fxr

with open('english_ranked_words.json', 'r', encoding='utf-8') as file:
    english_word_data = json.load(file)

with open('output_english_ranked_words.json', 'r', encoding='utf-8') as file:
    output_english_ranked_data = json.load(file)

with open('sinhala_ranked_words.json', 'r', encoding='utf-8') as file:
    sinhala_word_data = json.load(file)

with open('output_sinhala_ranked_words.json', 'r', encoding='utf-8') as file:
    output_sinhala_ranked_data = json.load(file)

fxr_english = calculate_fx_r_stability(english_word_data, output_english_ranked_data)
fxr_sinhala = calculate_fx_r_stability(sinhala_word_data, output_sinhala_ranked_data)

english_mean, english_std = compute_statistics(fxr_english, 'English')
sinhala_mean, sinhala_std = compute_statistics(fxr_sinhala, 'Sinhala')