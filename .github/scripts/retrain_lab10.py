"""Train LAB10 longer and save outputs only after a complete Run All."""
from pathlib import Path
import nbformat

file = Path("LAB10/Lab10_Introduction_to_Machine_Translation-2.ipynb")
notebook = nbformat.read(file, as_version=4)
code = notebook.cells[17].source

assert 'epochs=15,' in code
assert 'task_model.compile(optimizer="adam"' in code
assert 'word_id = int(output[0, i].argmax())' in code

code = code.replace('task_model.compile(optimizer="adam"', 'task_model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.002)')
code = code.replace('epochs=15,', 'epochs=40,')
code = code.replace('monitor="val_loss", patience=3', 'monitor="val_loss", patience=5')
code = code.replace('print(f"Test token accuracy (without padding, teacher forcing): {token_accuracy:.3f}")',
                    'print(f"Test token accuracy (without padding, teacher forcing): {token_accuracy:.3f}")\n'
                    'unknown_id = task_fr_tokenizer.word_index["<unk>"]\n'
                    'unknown_rate = np.mean((test_predictions == unknown_id)[real_words])\n'
                    'print(f"Unknown-token prediction rate: {unknown_rate:.3f}")')
code = code.replace('word_id = int(output[0, i].argmax())',
                    '# Do not generate padding or the unknown-word token\n'
                    '        next_word_probs = output[0, i].copy()\n'
                    '        next_word_probs[0] = 0\n'
                    '        next_word_probs[task_fr_tokenizer.word_index["<unk>"]] = 0\n'
                    '        word_id = int(next_word_probs.argmax())')
code += '''
print("Example from the training set (for comparison):")
print("English:", eng_train_text[0])
print("Expected French:", fr_train_text[0])
print("Predicted French:", translate_sentence(eng_train_text[0]))
'''
notebook.cells[17].source = code
notebook.cells[18].source = (
    "**Task 2 — Observation:** I trained the encoder–decoder LSTM using teacher forcing, "
    "with start/end tokens and short sentence pairs from the given Kaggle dataset. "
    "The printed token accuracy excludes padding and uses the correct previous French words. "
    "The predicted translations below use greedy decoding without the correct French input. "
    "The decoder avoids outputting padding or the unknown-token ID, but it can still translate "
    "incorrectly. The unknown prediction rate is also shown separately. "
    "Three test examples are unseen during training; the final example is from the training data.\n"
)
for cell in notebook.cells:
    if cell.cell_type == "code":
        cell.execution_count = None
        cell.outputs = []
nbformat.write(notebook, file)
print("Prepared new LAB10 training code; notebook needs a full re-execution.")
