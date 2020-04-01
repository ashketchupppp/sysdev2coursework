import unittest
from cli import Command
from cli import InteractiveCommandLine
from cli import CmdQuit
from cli import CmdRestart

class CommandForTests(Command):
    def __init__(self, commandLine, variablesToRequest=[]):
        Command.__init__(self, 'test', variablesToRequest, commandLine)
        self.called = False
        self.gotData = False
    
    def commandBody(self, variables):
        """ Return a test code to the caller. """
        self.called = True
        try:
            x = variables['testdataname']
            self.gotData = True
        except:
            pass
        return 'test'

class TestCommand(unittest.TestCase):
    def test_constructor(self):
        """ Ensure the constructor sets variables up correctly """
        cmdLine = InteractiveCommandLine()
        variablesToRequest = ['var1', 'var2']
        cmd = CommandForTests(cmdLine, variablesToRequest)
        self.assertEqual(cmd.commandLine, cmdLine)
        self.assertEqual(variablesToRequest, cmd.variablesToRequest)

class TestQuit(unittest.TestCase):
    def test_returnQuit(self):
        """ Ensure that the quit command returns quit """
        cmdLine = InteractiveCommandLine()
        quitCmd = CmdQuit(cmdLine)
        try:
            quitCmd.call()
            # quit command did not throw, test failure
            self.assertEqual(True, False)
        except Exception as e:
            self.assertEqual(str(e), 'quit')
        
class CmdHelp(unittest.TestCase):
    def test_returnSuccess(self):
        """ Ensure that help returns success. """
        cmdLine = InteractiveCommandLine()
        self.assertEqual(cmdLine.callCommand('help'), 'success')
        
class TestRestart(unittest.TestCase):
    def test_returnRestart(self):
        """ Ensure that the quit command returns quit """
        cmdLine = InteractiveCommandLine()
        restartCmd = CmdRestart(cmdLine)
        try:
            restartCmd.call()
            # restart command did not throw, test failure
            self.assertEqual(True, False)
        except Exception as e:
            self.assertEqual(str(e), 'restart')
        
class TestCommandLine(unittest.TestCase):
    def test_constructor(self):
        """ Ensure the constructor sets variables up correctly and
            the default commands are added """
        cmdLine = InteractiveCommandLine()
        self.assertEqual(False, cmdLine.running)
        self.assertIn('quit', cmdLine.commands)
        self.assertIn('restart', cmdLine.commands)
        self.assertIn('help', cmdLine.commands)
        self.assertEqual({}, cmdLine.data)
        self.assertEqual('', cmdLine.welcomeMessage)
        
    def test_setWelcome(self):
        """ Ensure the command line allows you to set the welcome message """
        cmdLine = InteractiveCommandLine()
        cmdLine.setWelcome('testwelcome')
        self.assertEqual(cmdLine.welcomeMessage, 'testwelcome')
        
    def test_addData(self):
        """ Ensure that data is added to the data dict correctly """
        cmdLine = InteractiveCommandLine()
        cmdLine.addData('myint', 1)
        self.assertEqual(1, cmdLine.getData('myint'))
        
    def test_addCommand(self):
        """ Ensure that commands are added correctly """
        cmdLine = InteractiveCommandLine()
        testCmd = CommandForTests(cmdLine)
        cmdLine.addCommand(testCmd)
        self.assertEqual(cmdLine.commandExists('test'), True)
        
    def test_callCommand(self):
        """ Ensure that the command is called by call command method. """
        cmdLine = InteractiveCommandLine()
        testCmd = CommandForTests(cmdLine)
        cmdLine.addCommand(testCmd)
        cmdLine.callCommand('test')
        self.assertEqual(testCmd.called, True)
        
    def test_getRequestedVariables(self):
        """ Ensure that the variables requested from the command line
            are recieved when requested. """
        cmdLine = InteractiveCommandLine()
        cmdLine.addData('testdata', 1)
        cmdLine.addData('testdata2', 2)
        requested = ['testdata', 'testdata2']
        result = cmdLine.getRequestedVariables(requested)
        self.assertEqual(1, result['testdata'])
        self.assertEqual(2, result['testdata2'])
        
    def test_commandRecievesRequestedData(self):
        """ Ensure that the command gets the data from the command lines
            data dictionary that it is set to request """
        cmdLine = InteractiveCommandLine()
        cmdLine.addData('testdataname', 'testdata')
        testCmd = CommandForTests(cmdLine, ['testdataname'])
        cmdLine.addCommand(testCmd)
        cmdLine.callCommand('test')
        self.assertEqual(testCmd.called, True)
        self.assertEqual(testCmd.gotData, True)

# this is required to be able to run the tests
if __name__ == '__main__':
    unittest.main()