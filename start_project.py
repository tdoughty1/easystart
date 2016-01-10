#!/usr/bin/env python

# Standard Libraries
import os

# Custom Modules
import write_setup

# Define a simple namespace class to hold config options
class Config():
    pass

def main():
    
    # Create config object
    config = Config()
    
    ## Get input from user
    
    # Project Info
    config.project_name = raw_input('Input Project Name: ')
    config.author = raw_input('Author Name: ')
    config.email = raw_input('Author Email: ')
    config.version = raw_input('Starting Version: ')

    # Check if user wants to use version control
    vcsToken = raw_input('Implement Version Control: ')
    config.vcsFlag = vcsToken in ['1','T','True','t','true','y','Y','yes','Yes'] 

    # Check which vcs
    if config.vcsFlag:
        print 'Currently there is only support for Git'
        
        #TODO Support Additional vcs options
    
    # Check for hosting choice
    hostToken = raw_input('Do you want to host the code? ')
    config.hostFlag = hostToken in ['1','y','Y','yes','Y']
    
    # Check which host
    if config.hostFlag:
        config.hostOpt = raw_input('Bitbucket (1) or Github (2)? ')
        config.hostID = raw_input('Username: ')
        config.hostProject = raw_input('Project Repo name (' + project_name.lower() + '): ') 
        print 'For the automated hosting option to function, the remote repository should already be initialized.'
        
        config.hostInit = raw_input('Has remote repository been created?') 
    
        

    #TODO Add automatic license implementation
    # License information

    # Create project repo
    os.mkdir(config.project_name)
    
    # Move into repo
    os.chdir(config.project_name)
    
    # Add Setup files
    write_setup.write_python(config)
    
    f = open('setup.cf','w')
    f.write('')
    f.close()

    # Add Readme
    f = open('README.rst','w')
    f.write('')
    f.close()

    # Add Manifest
    f = open('MANIFEST.in','w')
    f.write('')
    f.close()

    # Add License
    f = open('LICENSE','w')
    f.write('')
    f.close()
    
    # Add Todo
    f = open('TODO.md','w')
    f.write('')
    f.close()
    
    # Add Requirements
    f = open('requirements.txt','w')
    f.write('')
    f.close()
    
    # Make docs directory
    os.mkdir('docs')
    
    # Make tests directory
    os.mkdir('tests')
    
    # Make project module folder
    os.mkdir(config.project_name.lower())
    
    # Move into project module folder
    os.chdir(config.project_name.lower())
    
    # Make into a module
    f = open('__init__.py','w')
    f.write('')
    f.close()

if __name__ == '__main__':
    main()

