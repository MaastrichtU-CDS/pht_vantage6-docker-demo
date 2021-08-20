# Uncomment and run to install the vantage6 client
if (!('vtg' %in% installed.packages())) {
  devtools::install_github('IKNL/vtg.basic', subdir='src')
}


setup.client <- function() {
  # Define parameters
  username <- "node1-user"
  password <- "node1-password"
  host <- 'http://localhost:5000'
  api_path <- '/api'
  
  # Create the client
  client <- vtg::Client$new(host, api_path=api_path)
  client$authenticate(username, password)
  
  return(client)
}

# Create a client
client <- setup.client()

# Get a list of available collaborations
print( client$getCollaborations() )

# Should output something like this:
#   id     name
# 1  1 ZEPPELIN
# 2  2 PIPELINE

# Select a collaboration
client$setCollaborationId(1)

client$set.task.image(
  'jaspersnel/vtg.tpl',
  task.name="colnames"
)

# Run the bayesian network algorithm
client$setUseMasterContainer(T)
result <- client$call('colnames')

print("Results:")
print(result)