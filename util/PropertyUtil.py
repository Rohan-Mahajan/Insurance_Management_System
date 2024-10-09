class PropertyUtil :
    
    @staticmethod
    def getConnectionString() :
        return (
            'Driver={SQL Server};'
            'Server=MYIDEAPAD\SQLEXPRESS;'  
            'Database=InsuranceManagementSystem;'
            'Trusted_Connection=yes;'
        )