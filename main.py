from dao.InsuranceServiceImpl import InsuranceServiceImpl
from entity.policy import Policy
from exception.policyException import PolicyNotFoundException

class PolicyManagementSystem:  # Renamed class to give it a more descriptive name
    def __init__(self):
        self.insurance_handler = InsuranceServiceImpl()  # Renamed insurance_service to insurance_handler

    def display_menu(self):
        # Method to display the main menu and process user input
        while True:
            print("\n===== Insurance Management System Menu =====")
            print("1. Create New Policy")
            print("2. Retrieve Policy by ID")
            print("3. View All Policies")
            print("4. Modify Existing Policy")
            print("5. Remove Policy")
            print("6. Exit Application")

            user_choice = input("Select an option: ")

            if user_choice == '1':
                self.initiate_policy_creation()
            elif user_choice == '2':
                self.fetch_policy()
            elif user_choice == '3':
                self.view_all_policies()
            elif user_choice == '4':
                self.modify_policy()
            elif user_choice == '5':
                self.remove_policy()
            elif user_choice == '6':
                print("Exiting the system...")
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def initiate_policy_creation(self):
        # Method to handle new policy creation
        try:
            policy_identifier = int(input("Enter policy ID: "))
            policy_name = input("Enter policy name: ")
            policy_premium = float(input("Enter premium amount: "))
            policy_coverage = float(input("Enter coverage amount: "))

            new_policy = Policy(policy_identifier, policy_name, policy_premium, policy_coverage)
            result = self.insurance_handler.createPolicy(new_policy)

            if result:
                print("Policy created successfully.")
            else:
                print("Failed to create the policy.")
        except Exception as e:
            print(f"Error during policy creation: {e}")

    def fetch_policy(self):
        # Method to retrieve a policy by its ID
        try:
            policy_identifier = int(input("Enter policy ID: "))
            retrieved_policy = self.insurance_handler.getPolicy(policy_identifier)

            if retrieved_policy:
                print(retrieved_policy)
        except Exception as e:
            print(f"Error during policy retrieval: {e}")

    def view_all_policies(self):
        # Method to view all policies
        try:
            policies_list = self.insurance_handler.getAllPolicies()

            if policies_list:
                print("\nAll Available Policies:")
                for policy in policies_list:
                    print(policy)
            else:
                print("No policies available.")
        except Exception as e:
            print(f"Error during retrieval of policies: {e}")

    def modify_policy(self):
        # Method to update an existing policy
        try:
            policy_identifier = int(input("Enter policy ID to update: "))
            existing_policy = self.insurance_handler.getPolicy(policy_identifier)

            if existing_policy:
                print(f"Current details for Policy ID {policy_identifier}: {existing_policy}")

                # Updating fields with user input or keeping existing values
                updated_name = input(f"Enter new policy name (current: {existing_policy.get_plan_name()}): ") or existing_policy.get_plan_name()
                updated_premium = float(input(f"Enter new premium amount (current: {existing_policy.get_premium_cost()}): ") or existing_policy.get_premium_cost())
                updated_coverage = float(input(f"Enter new coverage amount (current: {existing_policy.get_coverage_limit()}): ") or existing_policy.get_coverage_limit())

                # Apply updates
                existing_policy.set_plan_name(updated_name)
                existing_policy.set_premium_cost(updated_premium)
                existing_policy.set_coverage_limit(updated_coverage)

                result = self.insurance_handler.updatePolicy(existing_policy)
                if result:
                    print(f"Policy {policy_identifier} updated successfully.")
                else:
                    print("Failed to update the policy.")
            else:
                print(f"Policy with ID {policy_identifier} not found.")
        except Exception as e:
            print(f"Error during policy modification: {e}")

    def remove_policy(self):
        # Method to delete a policy by its ID
        try:
            policy_identifier = int(input("Enter policy ID to delete: "))
            result = self.insurance_handler.deletePolicy(policy_identifier)

            if result:
                print(f"Policy {policy_identifier} deleted successfully.")
            else:
                print(f"Failed to delete policy with ID {policy_identifier}.")
        except Exception as e:
            print(f"Error during policy deletion: {e}")

def main():
    # Main function to start the application
    policy_manager = PolicyManagementSystem()  # Instantiating PolicyManagementSystem
    policy_manager.display_menu()  # Call to display the menu

if __name__ == "__main__":
    main()
