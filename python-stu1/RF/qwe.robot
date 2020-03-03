*** Test Cases ***
#example
#    for ${element}  in  @{elements}
#        start element   ${element}
#    end

example1
    :For    ${animal}    in  .  猫  狗  猪
    \   Log To Console   ${animal}

    log to console       循环外面