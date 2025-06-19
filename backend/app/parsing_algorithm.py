def bottom_up_algorithm(action_table, goto_table, input):
    error_registry = {}
    error_id_counter = 1

    stack = ["0"]
    pointer = 0

    aux_cont = 0

    input_tape = input.split(" ")
    input_tape.append("$")

    detailed_steps = [
        {
            "stepByStep": ["Início da análise"],
            "stepByStepDetailed": [["A análise sintática foi iniciada."]],
            "stack": stack[::-1].copy(),
            "input": input_tape.copy(),
            "pointer": pointer,
            "stepMarker": ["", ""],
        }
    ]

    run = True
    while run:
        aux_cont += 1
        if aux_cont > 1000:
            break

        step_by_step = []
        step_by_step_detailed = []

        action = ["", ""]
        action[0] = int(stack[-1]) + 1
        action[1] = input_tape[pointer]

        if action[1] not in action_table:
            step_by_step.append(f"Erro léxico: símbolo '{action[1]}' inválido.")
            step_by_step_detailed.append(
                [
                    f"O símbolo '{action[1]}' não pertence ao alfabeto da linguagem.",
                    "A análise foi encerrada por erro léxico.",
                ]
            )
            detailed_steps.append(
                {
                    "stepByStep": step_by_step,
                    "stepByStepDetailed": step_by_step_detailed,
                    "stack": stack[::-1].copy(),
                    "input": input_tape.copy(),
                    "pointer": pointer,
                    "stepMarker": ["", ""],
                }
            )
            break

        action_movement = action_table[action[1]][action[0]].split("[")
        action_movement[0] = action_movement[0].strip()
        if action_movement[0] not in ["ACEITO"] and "ERRO" not in action_movement[0]:
            action_movement[1] = action_movement[1].strip("]").strip()

        step_by_step.append(f"AÇÃO[{action[1]}, {action[0] -1}] => {action_movement}")
        step_by_step_detailed.append(
            [
                "Consulta na tabela de ações.",
                f"Coluna '{action[1]}', Linha '{action[0] -1}', ação: {action_movement}",
            ]
        )
        detailed_steps.append(
            {
                "stepByStep": step_by_step.copy(),
                "stepByStepDetailed": step_by_step_detailed.copy(),
                "stack": stack[::-1].copy(),
                "input": input_tape.copy(),
                "pointer": pointer,
                "stepMarker": [action[1], action[0] -1],
            }
        )

        if action_movement[0].startswith("REDUZIR"):
            array_action_movement = action_movement[1].split(" ")

            reduce_elements = array_action_movement[2:]
            qt_unstack = 2 * len(reduce_elements)

            for _ in range(qt_unstack):
                if stack:
                    stack.pop()

            step_by_step.append(f"Desempilhar {qt_unstack} elementos.")
            step_by_step_detailed.append(
                [
                    "Desempilhar elementos correspondentes à produção.",
                    f"Número de desempilhamentos: {qt_unstack}.",
                ]
            )

            transition = [int(stack[-1]) + 1, array_action_movement[0]]
            goto_movement = goto_table[transition[1]][transition[0]]

            step_by_step.append(
                f"TRANSIÇÃO[{transition[1]}, {transition[0] -1}] => {goto_movement}"
            )
            step_by_step_detailed.append(
                [
                    "Consulta na tabela GOTO.",
                    f"Coluna '{transition[1]}', Linha '{transition[0] -1}', resultado: {goto_movement}.",
                ]
            )

            stack_up = str(int(goto_movement[10:].split(" ")[0]))
            stack.append(array_action_movement[0])
            stack.append(stack_up)

            step_by_step.append(f"Empilhar {array_action_movement[0]}, {stack_up}.")
            step_by_step_detailed.append(
                [
                    "Empilhar não-terminal da redução e novo estado.",
                    f"Empilhado: {array_action_movement[0]} e {stack_up}.",
                ]
            )

        elif action_movement[0].startswith("EMPILHAR"):
            stack.append(action[1])
            stack.append(action_movement[1])

            step_by_step.append(f"Empilhar: {action[1]} e {action_movement[1]}")
            step_by_step_detailed.append(
                [
                    "Ação de empilhar (SHIFT).",
                    f"Empilha '{action[1]}' e estado '{action_movement[1]}'.",
                ]
            )
            pointer += 1
            if pointer >= len(input_tape):
                break

        elif action_movement[0] == "ACEITO":
            step_by_step.append("A entrada foi aceita.")
            step_by_step_detailed.append(["Análise sintática concluída com sucesso."])
            detailed_steps.append(
                {
                    "stepByStep": step_by_step,
                    "stepByStepDetailed": step_by_step_detailed,
                    "stack": stack[::-1].copy(),
                    "input": input_tape.copy(),
                    "pointer": pointer,
                    "stepMarker": ["", ""],
                }
            )
            break

        elif action_movement[0] == "ERRO!":
            current_state = action[0]
            input_symbol = action[1]
            error_key = (current_state, input_symbol)

            if error_key not in error_registry:
                error_registry[error_key] = f"ERRO{error_id_counter}"
                error_id_counter += 1

            error_label = error_registry[error_key]
            action_movement[0] = error_label

            step_by_step.append(f"Erro sintático identificado: {error_label}.")
            step_by_step_detailed.append(
                [f"Ação inválida para símbolo '{input_symbol}' no estado {current_state -1}."]
            )

            valid_symbols = [
                sym
                for sym in action_table.keys()
                if action_table[sym].get(current_state) not in ["ERRO!", "", None]
            ]

            if valid_symbols:
                replacement = valid_symbols[0]
                old_symbol = input_tape[pointer]
                step_by_step.append(
                    f"Substituir '{old_symbol}' por '{replacement}' na posição {pointer}."
                )
                step_by_step_detailed.append(
                    [
                        f"O símbolo '{old_symbol}' é inválido nesse contexto.",
                        f"Substituído por '{replacement}' para tentar continuar.",
                    ]
                )
                input_tape[pointer] = replacement
            else:
                panic = False
                while len(stack) > 2:
                    popped_state = stack.pop()
                    popped_symbol = stack.pop()

                    current_state = int(stack[-1]) + 1

                    if action_table.get(input_symbol, {}).get(current_state) not in ["ERRO!", "", None]:
                        step_by_step.append(
                            f"Panic mode: Após desempilhar, estado {current_state -1} aceita '{input_symbol}'."
                        )
                        panic = True
                        break
                    else:
                        step_by_step.append(
                            f"Panic mode: desempilhando '{popped_symbol}', estado {popped_state}."
                        )

                if not panic:
                    if input_tape[pointer] != "$":
                        removed_symbol = input_tape.pop(pointer)
                        step_by_step.append(
                            f"Panic mode: símbolo '{removed_symbol}' removido da fita para tentar recuperação."
                        )
                        if pointer >= len(input_tape):
                            input_tape.append("$")
                    else:
                        step_by_step.append(
                            "Erro irreparável. Não foi possível recuperar. Encerrando análise."
                        )
                        step_by_step_detailed.append(
                            ["Encerramento definitivo após tentativa de recuperação falha."]
                        )
                        detailed_steps.append(
                            {
                                "stepByStep": step_by_step.copy(),
                                "stepByStepDetailed": step_by_step_detailed.copy(),
                                "stack": stack[::-1].copy(),
                                "input": input_tape.copy(),
                                "pointer": pointer,
                                "stepMarker": ["", ""],
                            }
                        )
                        break

            detailed_steps.append(
                {
                    "stepByStep": step_by_step.copy(),
                    "stepByStepDetailed": step_by_step_detailed.copy(),
                    "stack": stack[::-1].copy(),
                    "input": input_tape.copy(),
                    "pointer": pointer,
                    "stepMarker": ["", ""],
                }
            )
            continue

        else:
            return {"Erro": "Houve um erro inesperado durante a análise!"}

        detailed_steps.append(
            {
                "stepByStep": step_by_step.copy(),
                "stepByStepDetailed": step_by_step_detailed.copy(),
                "stack": stack[::-1].copy(),
                "input": input_tape.copy(),
                "pointer": pointer,
                "stepMarker": ["", ""],
            }
        )

    return detailed_steps