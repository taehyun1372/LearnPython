def simple_assembler(program):
	# return a dictionary with the registers
	return {}


if __name__ == "__main__":
    code = '''\
    mov a 5
    inc a
    dec a
    dec a
    jnz a -1
    inc a'''
    result = code.splitlines()
    print(result)