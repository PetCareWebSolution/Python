from graphviz import Digraph

# Create a new directed graph
dot = Digraph()

# Add nodes for each activity
dot.node('Start', 'Start')
dot.node('ViewAvailablePets', 'View Available Pets')
dot.node('AdoptPets', 'Adopt Pets')
dot.node('MakePayment', 'Make Payment')
dot.node('BookVetAppointment', 'Book Vet Appointment')
dot.node('ManageProfile', 'Manage Profile')
dot.node('ViewEvents', 'View Events')
dot.node('SaveFavorites', 'Save Favorites')
dot.node('ProvideFeedback', 'Provide Feedback')
dot.node('End', 'End')

# Add edges between the nodes to represent the sequence of activities
dot.edge('Start', 'ViewAvailablePets')
dot.edge('ViewAvailablePets', 'AdoptPets')
dot.edge('AdoptPets', 'MakePayment')
dot.edge('MakePayment', 'BookVetAppointment')
dot.edge('BookVetAppointment', 'ManageProfile')
dot.edge('ManageProfile', 'ViewEvents')
dot.edge('ViewEvents', 'SaveFavorites')
dot.edge('SaveFavorites', 'ProvideFeedback')
dot.edge('ProvideFeedback', 'End')

# Render and display the graph
dot.render('/mnt/data/petcare_hub_activity_diagram', format='png', cleanup=True)
'/mnt/data/petcare_hub_activity_diagram.png'
