import traceback
import sys

class Command:
    """ Command class. All commands must inherit from this class.
        When a command is called by the user, its corresponding
        command class is found and calls the call method. """
    def __init__(self, name, variablesToRequest, commandLine, description=''):
        self.name = name
        self.variablesToRequest = variablesToRequest
        self.commandLine = commandLine
        self.description = description
    
    def call(self):
        """ Sets everything up for the command. Gets variables from the
            command line.""" 
        requestedVariables = self.commandLine.getRequestedVariables(self.variablesToRequest) 
        result = self.commandBody(requestedVariables) 
        return result

    def commandBody(self, variables):
        """ Command child classes must override this method. """
        return 0
        
    def prompt(self, message):
        """ Prompts user for input. """
        print(message)
        userinput = input(' > ')
        # check for speical commands, quit and restart
        self.commandLine.processSpecialCommands(userinput)
        return userinput
    
class CmdQuit(Command):
    def __init__(self, commandLine):
        Command.__init__(self, 'quit', [], commandLine, 'Exits the whole program')
        
    def commandBody(self, variables):
        """ Return a quit code to the main program. """
        # use exception here to cause a premature exit
        # this will allow commands to exit whilst still in
        # the command function without the commands needing
        # to directly program the exit in themselves
        raise Exception('quit')
        
class CmdRestart(Command):
    def __init__(self, commandLine):
        Command.__init__(self, 'restart', [], commandLine, 'Exits the current command')
    
    def commandBody(self, variables):
        """ Return a restart code to the main program. """
        # use exception here to cause a premature exit
        # this will allow commands to exit whilst still in
        # the command function without the commands needing
        # to directly program the exit in themselves
        print('Restarting...')
        raise Exception('restart')
        
class CmdHelp(Command):
    def __init__(self, commandLine):
        Command.__init__(self, 'help', [], commandLine, 'Outputs this help message')
    
    def commandBody(self, variables):
        """ Print a list of commands and return a help code to the main program. """
        try:
            for cmd in self.commandLine.commands:
                print('{} - {}'.format(cmd, self.commandLine.commands[cmd].description))
            return 'success'
        except:
            return 'failure'

class InteractiveCommandLine:
    """ Interactive command line class, manages user input, calling
        commands functions and error handling. """
    def __init__(self):
        """ Constructor function to initialise the objects' state. """
        self.running = False
        self.commands = {}
        self.data = {}
        self.welcomeMessage = ""
        self.specialCommands = ['quit', 'restart']
        
        # add the default commands
        self.addCommand(CmdHelp(self))
        self.addCommand(CmdQuit(self))
        self.addCommand(CmdRestart(self))

    def setWelcome(self, message):
        """ Set the welcome message to whatever is passed. """
        self.welcomeMessage = message
        
    def outputHelp(self):
        """ Outputs the list of all commands and their descriptions. """

    def prompt(self):
        """This is a function to prompt the user for input and format the user interface correctly. """
        userinput = input(" > ")
        userinput = userinput.lower()
        return userinput
        
    def getData(self, name):
        """ Retrieve some data from the data dictionary """
        return self.data[name]

    def addData(self, name, data):
        """ Adds some stored data that can be passed to the commands. """
        self.data[name] = data

    def addCommand(self, commandObject):
        """ Creates a new command using the commandObject passed. """
        self.commands[commandObject.name] = commandObject 
        
    def commandExists(self, commandName):
        """ Returns true or fales depending on if a command exists or not """
        return True if commandName in self.commands else False

    def getRequestedVariables(self, variableList):
        """ Gets a list of the requested variables in the variableList. """
        variables = {} 
        for var in variableList:
            try:
                variables[var] = self.data[var]
            except:
                # variable doesn't exist
                pass
        return variables
        
    def processAllCommands(self, userinput):
        """ Method to process the users input and execute a command if necessary. """
        returnCode = ''
        if self.commandExists(userinput):
            for cmd in self.commands:
                if userinput == cmd:
                    returnCode = self.callCommand(cmd)
        else:
            print('That is not a command. Type help for a list of commands.')
        return returnCode
        
    def processSpecialCommands(self, userinput):
        """ Method to process the users input and execute a special command if necessary.
            This is for use inside custom commands only. Use processAllCommands for the top level
            command prompt. """
        returnCode = ''
        if self.commandExists(userinput):
            for cmd in self.specialCommands:
                if userinput == cmd:
                    returnCode = self.callCommand(cmd)
        return returnCode
            
    def callCommand(self, commandName):
        """ Calls a command by name """
        return self.commands[commandName].call()

    def run(self):
        """ Starts the cycle of input and command processing. """
        self.running = True
        print(self.welcomeMessage)
        self.callCommand('help')
        while self.running:
            try:
                command = self.prompt()
                returnCode = self.processAllCommands(command)
            except KeyboardInterrupt as exception:
                # do nothing for a keyboard interrupt
                pass
            except Exception as exception:
                if str(exception) == 'quit':
                    self.running = False
                elif str(exception) == 'restart':
                    pass
                else:
                    # unknown error, print it
                    traceback.print_exc()
            print()
                