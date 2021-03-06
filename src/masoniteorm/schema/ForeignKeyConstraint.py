class ForeignKeyConstraint:
    def __init__(self, column, foreign_table, foreign_column):
        self.column = column
        self.foreign_table = foreign_table
        self.foreign_column = foreign_column
        self.delete_action = None
        self.update_action = None

    def references(self, foreign_column):
        self.foreign_column = foreign_column
        return self

    def on(self, foreign_table):
        self.foreign_table = foreign_table
        return self

    def on_delete(self, action):
        self.delete_action = action
        return self

    def on_update(self, action):
        self.update_action = action
        return self
