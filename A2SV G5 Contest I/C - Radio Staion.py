def add_comments_to_nginx_config(server_info, commands):
    server_ip_to_name = {ip: name for name, ip in server_info}
    commented_commands = []

    for command in commands:
        ip = command.split()[-1].strip(';')
        name = server_ip_to_name.get(ip)
        if name:
            command += f"; #{name}"
        commented_commands.append(command)

    return commented_commands

if __name__ == "__main__":
    n, m = map(int, input().split())
    server_info = []
    for _ in range(n):
        name, ip = input().split()
        server_info.append((name, ip))
    commands = [input().rstrip(';') for _ in range(m)]

    commented_commands = add_comments_to_nginx_config(server_info, commands)
    for command in commented_commands:
        print(command)