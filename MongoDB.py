from pymongo import MongoClient
from bson import ObjectId

client = MongoClient ("mongodb://localhost:27017") #local mongodb connection
db = client["wasteManagementDB" ]

#Display all documents
def display_documents(collection):
    for item in collection.find():
        print(item)

#Add a document
def add_document(collection):

    if collection.name =="collectionVehicles":
        vehicle_id = input("Enter Vehicle ID:")
        registration = input("Enter registration:")
        vehicle_type = input("Enter vehicle type:")
        fuel_type = input("Enter fuel type:")

        collection.insert_one({
            "vehicleID": vehicle_id,
            "registration": registration,
            "vehicleType": vehicle_type,
            "fuelType": fuel_type
        })    

    else:  
        route_id = input("Enter route ID: ")
        route_name = input("Enter route name: ")
        city_zone = input("Enter city zone: ")
        waste_type = input("Enter waste type: ")

        collection.insert_one({
            "routeID": route_id,
            "routeName": route_name,
            "cityZone": city_zone,
            "wasteType": waste_type
        })

    print("Document added successfully")
              

# Update a document
def update_document(collection):
    document_id = input("Enter Document ID: ")

    if not ObjectId.is_valid(document_id):
        print("Invalid Document ID")
        return

    if collection.name == "collectionVehicles":
        new_value = input("Enter new fuel type: ")
        field = "fuelType"
    else:
        new_value = input("Enter new waste type: ")
        field = "wasteType"

    result = collection.update_one(
        {"_id": ObjectId(document_id)},
        {"$set": {field: new_value}}
    )

    if result.matched_count > 0:
        print("Document updated")
    else:
        print("Document not found.")
# Delete a document
def delete_document(collection):
    document_id = input("Enter Document ID: ")

    if not ObjectId.is_valid(document_id):
        print("Invalid Document ID")
        return

    result = collection.delete_one(
        {"_id": ObjectId(document_id)}
    )

    if result.deleted_count > 0:
        print("Document deleted")
    else:
        print("Document not found.")

# Search for documents

def search_documents(collection):
    if collection.name == "collectionVehicles":
        keyword = input("Enter fuel type to search: ")
        field = "fuelType"
    else:
        keyword = input("Enter waste type to search: ")
        field = "wasteType"

    for item in collection.find({field: keyword}):
        print(item)
                   

#main menu
def main():
    print("Welcome to the city council Waste Management System!")

    while True:
        print("Select a collection:")
        print("1. Collection vehicles")
        print("2. Collection Routes")
        print("3. Exit System")

        choice = input("Enter choice: ")

        if choice == "1":
            collection = db["collectionVehicles"]
        elif choice == "2":
            collection = db["collectionRoutes"]
        elif choice == "3":
            print("Goodbye")
            break
        else:
            print("Invalid choice. Please try again.")
            continue

        print("Main Menu")
        print("1. Display all documents")
        print("2. Add a new document")
        print("3. Update a document")
        print("4. Delete a document")
        print("5. Search for documents")
        print("6. Exit")

        action = input("Enter your choice (1-6): ")

        if action == "1":
            display_documents(collection)
        elif action == "2":
            add_document(collection)
        elif action == "3":
            update_document(collection)
        elif action == "4":
            delete_document(collection)
        elif action == "5":
            search_documents(collection)
        elif action == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

main()

             


