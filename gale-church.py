import math
import json

# Gale-Church Sentence Alignment Algorithm
def gale_church_alignment(src_sentences, tgt_sentences):
    aligned_pairs = []
    
    for i in range(min(len(src_sentences), len(tgt_sentences))):
        src_len = len(src_sentences[i])
        tgt_len = len(tgt_sentences[i])
        
        # Calculate alignment score (absolute difference in sentence length)
        score = abs(src_len - tgt_len)
        
        # Consider aligned if lengths are close enough
        if score <= (0.3 * max(src_len, tgt_len)):  # Threshold: 30% of the longer sentence's length
            aligned_pairs.append((src_sentences[i], tgt_sentences[i]))
        else:
            aligned_pairs.append(("MISMATCH", src_sentences[i], tgt_sentences[i]))
    
    return aligned_pairs

# Load preprocessed sentences from the previous step
with open('preprocessed_sentences.json', 'r', encoding='utf-8') as file:
    preprocessed_data = json.load(file)

# Separate Sinhala and English sentences
sinhala_sentences = [' '.join(pair['Sinhala']) for pair in preprocessed_data]
english_sentences = [' '.join(pair['English']) for pair in preprocessed_data]

# Perform alignment
aligned_sentences = gale_church_alignment(sinhala_sentences, english_sentences)

# Save the alignment results
with open('aligned_sentences.json', 'w', encoding='utf-8') as out_file:
    json.dump(aligned_sentences, out_file, ensure_ascii=False, indent=4)

# Print some of the alignments
for aligned_pair in aligned_sentences[:10]:
    print(aligned_pair)
