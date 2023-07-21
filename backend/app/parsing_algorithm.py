def bottom_up_algorithm(action_table, goto_table, input):
    stack = ['0']
    pointer = 0

    input_tape = input.split(' ')
    input_tape.append('$')

    step_number = 0

    # Gardar os passos
    step = 0
    steps = {step: {'stack': stack.copy(), 'input': input_tape, 'step_action': []}}
    detailed_steps = [{'label': 'Inicio de analise', 'stack': stack.copy(), 
                       'input': input_tape.copy(), 'stepNumber': step_number}]
    
    run = True
    while (run == True):
        action = ['', '']
        transition = ['', '']
        step += 1
        aux_stack = []
        for i in stack:
            aux_stack.append(i)

        action[0] = int(stack[len(stack) - 1]) + 1
        action[1] = input_tape[pointer]
        action_movement = action_table[action[1]][action[0]].split('(')

        step_number+=1

        detailed_steps.append({'label': f'AÇÃO[{action[1]}, {action[0]}] => {action_movement}', 
                                'stack': stack.copy(), 'input': input_tape.copy(), 
                                'stepNumber': step_number})

        match action_movement[0][0]:
            case 'r':
                action_movement[1] = action_movement[1][:-1]
                reduce_div = action_movement[1].split(' ')
                qt_unstack = 2 * len(reduce_div[2:])

                for i in range(qt_unstack):
                    stack.pop()

                detailed_steps.append({'label': f'Desempilhar {qt_unstack}', 
                                        'stack': stack.copy(), 'input': input_tape.copy(), 
                                        'stepNumber': step_number})

                transition[0] = int(stack[len(stack) - 1]) + 1
                transition[1] = reduce_div[0]
                goto_movement = goto_table[transition[1]][transition[0]]

                detailed_steps.append({'label': f'TRANSIÇÃO[{transition[1]}, {transition[0]}] => {goto_movement}', 
                                        'stack': stack.copy(), 'input': input_tape.copy(), 
                                        'stepNumber': step_number})
                if (goto_movement[0] == 's'):
                    stack.append(reduce_div[0])
                    stack.append(str(int(goto_movement[1:])))
                else:
                    steps[step] = {'stack': stack, 'input': input_tape[pointer:], 'step_action': ['Erro']}
                    break

                detailed_steps.append({'label': f'Empilhar {reduce_div[0]}, {str(int(goto_movement[1:]))}', 
                                        'stack': stack.copy(), 'input': input_tape.copy(), 
                                        'stepNumber': step_number})
                aux_step_action = [f'Reduzir: {action_movement[1]}',
                                   f'GOTO[{transition[0]},{transition[1]}] => {goto_movement}',
                                   f'Empilhar: {reduce_div[0]}, {str(int(goto_movement[1:]))}'
                                   ]
            case 's':
                stack.append(action[1])
                stack.append(action_movement[0][1])
                
                detailed_steps.append({'label': f'Empilhar: {action[1]}, {action_movement[0][1]}', 
                                        'stack': stack.copy(), 'input': input_tape.copy(), 
                                        'stepNumber': step_number})

                aux_step_action = [f'Empilhar: {action[1]}, {action_movement[0][1]}']
                pointer += 1
            case 'a':
                
                detailed_steps.append({'label': f'A entrada foi aceita!', 
                                        'stack': stack.copy(), 'input': input_tape.copy(), 
                                        'stepNumber': step_number})

                steps[step] = {'stack': [aux_stack], 'input': input_tape[pointer:], 'step_action': ['Aceita']}
                break
            case 'e':
                detailed_steps.append({'label': f'A entrada não está correta.', 
                                        'stack': stack.copy(), 'input': input_tape.copy(), 
                                        'stepNumber': step_number})

                print('Erro')
                steps[step] = {'stack': f'{aux_stack}', 'input': input_tape[pointer:], 'step_action': ['Erro']}
                break
            case _:
                return {'Erro': 'Houve um erro!'}

        if (action_movement[0][0] == 's'):
            steps[step] = {'stack': aux_stack, 'input': input_tape[pointer - 1:], 'step_action': aux_step_action}
        else:
            steps[step] = {'stack': aux_stack, 'input': input_tape[pointer:], 'step_action': aux_step_action}
    return detailed_steps