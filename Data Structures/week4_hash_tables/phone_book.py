# python3


class Query:
    """
    Query class which takes the input and saves in required format
    """
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


class Phonebook():

    def __init__(self):
        """
        Initialise a hash table ( Dictionary in python )
        """
        self.contacts = dict()

    def find(self, number):
        """
        Looks for a person with phone number.
        Replies with the person's name, or with string “not found”
        if there is no such person in the book.
        :param number:
        :return:
        """
        if number in self.contacts:
            return self.contacts[number]
        else:
            return "not found"

    def add(self, number, name):
        """
        Adds a person with name and phone number to the phone book.
        If there exists a user with such number already, then manager overwrites
        the corresponding name.
        :param number: number
        :param name: name
        :return:
        """
        self.contacts[number] = name

    def delete(self, number):
        """
        Erases a person with number from the phone book.
        If there is no such person, then the query is ignored.
        :param number: number
        :return:
        """
        if number in self.contacts:
            self.contacts.pop(number)


def read_queries():
    """
    Helper function to read queries
    :return:
    """
    n = int(input())
    return [Query(input().split()) for i in range(n)]


def write_responses(result):
    """
    Helper function to write queries on console
    :param result: list
    :return:
    """
    print('\n'.join(result))


def process_queries(queries):
    """
    Helper function to process the queries
    :param queries: Query class objects
    :return:
    """
    result = list()
    contacts = Phonebook()
    for cur_query in queries:
        if cur_query.type == 'add':
            contacts.add(cur_query.number, cur_query.name)
        elif cur_query.type == 'del':
            contacts.delete(cur_query.number)
        elif cur_query.type == 'find':
            result.append(contacts.find(cur_query.number))
    return result


if __name__ == '__main__':
    write_responses(process_queries(read_queries()))