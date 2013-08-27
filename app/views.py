from app import app

@app.route('/')
def index():
	return '''
		<html>
			<head>
				<title>Welcome to LocalJobs</title>
			</head>
			<body>
				<h1>Hello Folks !! Welcome to LocalJobs</h1>
			</body>
		</html>
	'''