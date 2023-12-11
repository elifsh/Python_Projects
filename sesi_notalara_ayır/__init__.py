from music21 import converter, stream

midi_file = "ses.midi"
score = converter.parse(midi_file)

notes = []
for element in score.recurse():
    if 'Note' in element.classes:
        notes.append(element.nameWithOctave)

output_file = "notalar.txt"  # Çıktı dosyasının adını belirtin
with open(output_file, "w") as file:
    for note in notes:
        file.write(note + "\n")

print(f"Notalar başarıyla '{output_file}' dosyasına kaydedildi.")


