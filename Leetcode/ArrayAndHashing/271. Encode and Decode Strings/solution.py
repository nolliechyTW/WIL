class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded_string = ''

        for s in strs:
            # Replace each occurrence of '/' with '//'
            # Then add our delimiter '/:' to the end
            encoded_string += s.replace('/', '//') + '/:'

        return encoded_string

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        decoded_strings = []
        current_string = ""

        # Initialize an index 'i' to start of the string
        i = 0
        while i < len(s):
            # If we encounter the delimiter '/:'
            if s[i:i+2] == '/:':
                decoded_strings.append(current_string)
                current_string = "" # Clear current_string for the next string
                i += 2 # Move the index 2 steps forward to skip the delimiter

            # If we encounter an escaped slash '//'
            elif s[i:i+2] == '//':
                # Add a single slash to the current_string
                current_string += '/'
                i += 2  # Move the index 2 steps forward to skip the escaped slash

            # Otherwise, just add the character to current_string
            else:
                current_string += s[i]
                i += 1

        # Return the list of decoded strings
        return decoded_strings
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))