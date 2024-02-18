class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # Separate logs into digit-logs and letter-logs
        digit_logs = []
        letter_logs = []
        
        for log in logs:
            # Check if the log is a digit-log or a letter-log
            if log.split()[-1].isdigit(): # log.split()[1].isdigit() also works
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        
        # Sort letter-logs: first by contents, then by identifier
        letter_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        
        # Return the sorted letter-logs followed by the original order digit-logs
        return letter_logs + digit_logs
