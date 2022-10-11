def combine_chunks(chunks):
	encoded_string = ""
	for char, counter in chunks:
		if counter <= 9:
			encoded_string += str(counter) + char
		else:
			whole_parts = counter // 9
			rest = counter % 9
			for _ in range(whole_parts):
				encoded_string += '9' + char
			encoded_string += str(rest) + char
	return encoded_string

# Time complexity - O(n)
# Space complexity - O(n)
def runLengthEncoding(string):
	idx = 0
	chunks = []
	while idx < len(string):
		current_char = string[idx]
		current_counter = 0
		flag = False
		while idx < len(string) and string[idx] == current_char:
			current_counter += 1
			idx += 1
			flag = True
		chunks.append((current_char, current_counter))
		if not flag:
			idx += 1
	return combine_chunks(chunks)
