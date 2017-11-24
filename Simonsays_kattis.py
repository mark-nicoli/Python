n = int(input())
simon_says = "Simon says"
for _ in range(n):
	s = input()
	if s.startswith(simon_says):
		print(s[len(simon_says):])
