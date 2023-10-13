def X=''
def ENV=['dev','sit','prod']
def DEPLOY=['locations','channels','both']

println "$(ENV)

pipelineJob(){
  parameters{
    stringParam('X','None','variable')
    choiceParam('env',ENV,'environment')
    choiceParam('deploy',DEPLOY,'environment')

  }
}

definition{
  scriptPath('JenkinsFile')
}
