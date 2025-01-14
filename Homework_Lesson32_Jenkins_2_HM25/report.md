<h1 align="center"> Задание:</h1>

1. Установите Jenkins на своей локальной машине или на удаленном
сервере, если у вас еще нет установленного экземпляра Jenkins.
2. Создайте новый Jenkins Pipeline. Можно использовать веб-интерфейс
Jenkins или описать Pipeline в виде кода на Groovy и загрузить его в
Jenkins.
3. Определите агента (agent) для вашего Pipeline. Вы можете выбрать
агента, такого как "any" для использования любого доступного агента
на хосте Jenkins, или указать другие опции, такие как использование
Docker-контейнера или облачного агента.
4. Определите этапы (stages) вашего Pipeline, такие как "Build", "Test" и
"Deploy". Вы можете добавить больше этапов в зависимости от вашего
проекта и требований.
5. В каждом этапе определите шаги (steps), которые должны быть
выполнены. Например, для этапа "Build" вы можете добавить шаги для
сборки вашего проекта, для этапа "Test" - шаги для запуска тестов, и
для этапа "Deploy" - шаги для развертывания вашего приложения на
целевой сервер.
6. Добавьте условия выполнения (when) для определенных этапов, если
это необходимо. Например, вы можете указать, что определенный этап
должен выполняться только при наличии определенной ветки в вашем
репозитории, или когда определенный параметр был установлен в
Jenkins.
7. Добавьте использование параметров (parameters) в вашем Pipeline, если
это требуется. Например, вы можете использовать параметры для
передачи настраиваемых значений, таких как версия приложения или
настройки окружения.
8. Добавьте обработку ошибок (error handling) в ваш Pipeline, такую как
проверку статуса выполнения шагов и обработку ошибок в случае
возникновения проблем. Например, вы можете добавить проверку
кодов возврата или вывода команд, и принимать соответствующие меры
в случае ошибок.
9. Запустите ваш Pipeline на Jenkins и отслеживайте выполнение этапов и
шагов в интерфейсе Jenkins. Просмотрите результаты выполнения и
проверьте, что ваш Pipeline выполняется успешно.
10.Документируйте ваш Pipeline, описав его структуру, шаги, условия
выполнения и параметры в документе или файле README. Укажите,
как запускать ваш Pipeline и какие ожидаемые результаты должны быть
получены.

 <h1 align="center"> Выполнение:</h1>

 Для Jenkins мастера использую локальную WSL машину на базе Ubuntu 24.02.
 После нескольких дней безуспешных попыток установки в качестве агента на локальную Ubuntu различных версий 18-24.02 на базе VMWare решаю установить локальную ВМ Ubuntu 20.04 server на базе Hyper-V и все получается.
    
        Конфиги машин:
            Мастер:
                eth0: 172.26.168.139/20
                ubuntu 24.02 server
            Агент:
                eth0: 172.26.168.138/20
                ubuntu 20.02 server

    Так же дополнительно подготавливаю машину агента, устанавливая туда все необходимы тулы, а именно

            #Java
            sudo apt udpate && sudo apt upgrade -t
            sudo apt install openjdk-21-jdk

            java -version

            openjdk version "21.0.5" 2024-10-15
            OpenJDK Runtime Environment (build 21.0.5+11-Ubuntu-1ubuntu124.04)
            OpenJDK 64-Bit Server VM (build 21.0.5+11-Ubuntu-1ubuntu124.04, mixed mode, sharing)

            #OpenSSH
            sudo apt install openss-server
            sudo systemstl enable sshd
    
    После того как машина агента готова, перехожу в браузере на 172.26.168.139:8080, логинюсь, захожу "Настроить jenkins" -> "Nodes" -> "New Node".

            Название: Agent_1
            Описание: node, ubuntu 20.04 server
            Кол-во процессоров-исполнителей: 2
            Директория: /home/node/
            Labels: node agent_1
            Использование: загружать настолько, насколько возможно
            Способо запуска: Launch agents via SSH
                Host: 172.16.168.138
                Creditials:
                Host Key Verification Strategy(здесь долго бился с know_host_file, в итоге сдался и сделал ручную): Manually provided key Verification Strategy
                SSH key: сгенерированый публичный RSA ключ хоста агента
        
    В итоге агент коннектится и синхронизируется:

            SSHLauncher{host='172.26.168.138', port=22, credentialsId='3897770b-54ea-4b17-b92f-085eb5f6b6e3', jvmOptions='', javaPath='', prefixStartSlaveCmd='', suffixStartSlaveCmd='', launchTimeoutSeconds=60, maxNumRetries=10, retryWaitTime=15, sshHostKeyVerificationStrategy=hudson.plugins.sshslaves.verifiers.ManuallyProvidedKeyVerificationStrategy, tcpNoDelay=true, trackCredentials=true}
            [01/10/25 13:20:51] [SSH] Opening SSH connection to 172.26.168.138:22.
            [01/10/25 13:20:55] [SSH] SSH host key matched the key required for this connection. Connection will be allowed.
            [01/10/25 13:20:55] [SSH] Authentication successful.
            [01/10/25 13:20:56] [SSH] The remote user's environment is:
            BASH=/usr/bin/bash
            BASHOPTS=checkwinsize:cmdhist:complete_fullquote:extquote:force_fignore:globasciiranges:hostcomplete:interactive_comments:progcomp:promptvars:sourcepath
            BASH_ALIASES=()
            BASH_ARGC=([0]="0")
            BASH_ARGV=()
            BASH_CMDS=()
            BASH_EXECUTION_STRING=set
            BASH_LINENO=()
            BASH_SOURCE=()
            BASH_VERSINFO=([0]="5" [1]="0" [2]="17" [3]="1" [4]="release" [5]="x86_64-pc-linux-gnu")
            BASH_VERSION='5.0.17(1)-release'
            DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
            DIRSTACK=()
            EUID=1000
            GROUPS=()
            HOME=/home/node
            HOSTNAME=ubuntu
            HOSTTYPE=x86_64
            IFS=$' \t\n'
            LANG=en_US.UTF-8
            LOGNAME=node
            MACHTYPE=x86_64-pc-linux-gnu
            MOTD_SHOWN=pam
            OPTERR=1
            OPTIND=1
            OSTYPE=linux-gnu
            PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
            PIPESTATUS=([0]="0")
            PPID=1066
            PS4='+ '
            PWD=/home/node
            SHELL=/bin/bash
            SHELLOPTS=braceexpand:hashall:interactive-comments
            SHLVL=1
            SSH_CLIENT='172.26.168.139 44032 22'
            SSH_CONNECTION='172.26.168.139 44032 172.26.168.138 22'
            TERM=dumb
            UID=1000
            USER=node
            XDG_RUNTIME_DIR=/run/user/1000
            XDG_SESSION_CLASS=user
            XDG_SESSION_ID=1
            XDG_SESSION_TYPE=tty
            _=']'
            [01/10/25 13:20:56] [SSH] Starting sftp client.
            [01/10/25 13:20:56] [SSH] Copying latest remoting.jar...
            Source agent hash is 28E3A3D224EDC0F7379AD95EB0A5D4B2. Installed agent hash is 28E3A3D224EDC0F7379AD95EB0A5D4B2
            Verified agent jar. No update is necessary.
            Expanded the channel window size to 4MB
            [01/10/25 13:20:56] [SSH] Starting agent process: cd "/home/node" && java  -jar remoting.jar -workDir /home/node -jar-cache /home/node/remoting/jarCache
            Jan 10, 2025 10:20:56 AM org.jenkinsci.remoting.engine.WorkDirManager initializeWorkDir
            INFO: Using /home/node/remoting as a remoting work directory
            Jan 10, 2025 10:20:56 AM org.jenkinsci.remoting.engine.WorkDirManager setupLogging
            INFO: Both error and output logs will be printed to /home/node/remoting
            <===[JENKINS REMOTING CAPACITY]===>channel started
            Remoting version: 3261.v9c670a_4748a_9
            Launcher: SSHLauncher
            Communication Protocol: Standard in/out
            This is a Unix agent
            Agent successfully connected and online
    
Создаю простой тестовый пйаплайн, который выглядит следующим образом:

        pipeline {
            agent {label 'agent_1'}
            
            stages{
                stage('build') {
                    steps {
                        sh 'echo "Build step is OK" >> basic_ppl.txt'
                    }
                }
                
                stage('test') {
                    steps {
                        sh 'echo "Test step is OK" >> basic_ppl.txt'
                    }
                }
                
                stage('deploy') {
                    steps {
                        sh 'echo "Deploy test is OK" >> basic_ppl.txt'
                    }
                }
            }
        }

Этот простой, базовый пайплайн создает текстовый файл и после каждого успешного шага добавляет строку.

        Started by user adminadmin
        [Pipeline] Start of Pipeline
        [Pipeline] node
        Running on Agent_1 in /home/node/workspace/basic ppl
        [Pipeline] {
        [Pipeline] stage
        [Pipeline] { (build)
        [Pipeline] sh
        + echo Build step is OK
        [Pipeline] }
        [Pipeline] // stage
        [Pipeline] stage
        [Pipeline] { (test)
        [Pipeline] sh
        + echo Test step is OK
        [Pipeline] }
        [Pipeline] // stage
        [Pipeline] stage
        [Pipeline] { (deploy)
        [Pipeline] sh
        + echo Deploy test is OK
        [Pipeline] }
        [Pipeline] // stage
        [Pipeline] }
        [Pipeline] // node
        [Pipeline] End of Pipeline
        Finished: SUCCESS
В итоге пайплайн выполняется и в рабочей дириктории агента создается текстовый документ с содержимым: 

        Build step is OK
        Test step is OK
        Deploy test is OK