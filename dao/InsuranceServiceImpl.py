from dao.IPolicyService import IPolicyService
from entity.policy import Policy
from util.dbConnection import DBConnection
from exception.policyException import PolicyNotFoundException

class InsuranceServiceImpl(IPolicyService):
    def __init__(self):
        self.connection = DBConnection.getConnection()  # Make sure you have the correct method name here
        if self.connection is None:
            raise Exception("Database connection could not be established.")
    def createPolicy(self, policy: Policy):
        try:
            cursor = self.connection.cursor()
            query = """insert into policy (policy_id, policy_name, premium_cost, coverage_limit)
                       VALUES (?, ?, ?, ?)"""
            cursor.execute(query, (policy.get_policy_id(), policy.get_plan_name(),
                                   policy.get_premium_cost(), policy.get_coverage_limit()))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error while creating policy: {e}")
            return False

    def getPolicy(self, policy_id: int):
        try:
            cursor = self.connection.cursor()
            query = """select * from policy where policy_id = ?"""
            cursor.execute(query, (policy_id,))
            row = cursor.fetchone()

            if row:
                policy = Policy(row[0], row[1], row[2], row[3])
                return policy
            else:
                raise PolicyNotFoundException(f"Policy with ID {policy_id} not found.")
        except PolicyNotFoundException as e:
            print(e)
            return None
        except Exception as e:
            print(f"Error while fetching policy: {e}")
            return None

    def getAllPolicies(self):
        try:
            cursor = self.connection.cursor()
            query = """select * from policy"""
            cursor.execute(query)
            rows = cursor.fetchall()

            policies = []
            for row in rows:
                policy = Policy(row[0], row[1], row[2], row[3])
                policies.append(policy)

            return policies
        except Exception as e:
            print(f"Error while fetching all policies: {e}")
            return []

    def updatePolicy(self, policy: Policy):
        try:
            cursor = self.connection.cursor()
            query = """update policy
                       set policy_name = ?, premium_cost = ?, coverage_limit = ?
                       where policy_id = ?"""
            cursor.execute(query, (policy.get_plan_name(), policy.get_premium_cost(),
                                   policy.get_coverage_limit(), policy.get_policy_id()))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error while updating policy: {e}")
            return False

    def deletePolicy(self, policy_id: int):
        try:
            cursor = self.connection.cursor()
            query = """delete from policy where policy_id = ?"""
            cursor.execute(query, (policy_id,))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error while deleting policy: {e}")
            return False
