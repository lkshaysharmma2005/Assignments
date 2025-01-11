def generate_portfolio():
    name = input("Enter your name: ")
    bio = input("Enter a short bio: ")
    skills = input("Enter your skills (comma-separated): ").split(",")
    projects = input("Enter your project names (comma-separated): ").split(",")

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{name}'s Portfolio</title>
    </head>
    <body>
        <h1>Welcome to {name}'s Portfolio</h1>
        <p>{bio}</p>
        <h2>Skills</h2>
        <ul>
            {''.join([f"<li>{skill.strip()}</li>" for skill in skills])}
        </ul>
        <h2>Projects</h2>
        <ul>
            {''.join([f"<li>{project.strip()}</li>" for project in projects])}
        </ul>
    </body>
    </html>
    """
    with open("portfolio.html", "w") as file:
        file.write(html)
    print("Portfolio generated as 'portfolio.html'!")

if __name__ == "__main__":
    generate_portfolio()
