# Trilha C#/.NET Sênior

Artefato de aprendizagem independente para quem quer evoluir dos fundamentos de C# até práticas de engenharia .NET sênior. A experiência é uma Blazor Web App em português brasileiro, com roadmap visual, aulas práticas, exemplos selecionados em C#, self-checks com feedback, capstone e progresso salvo no `localStorage` do navegador.

## Pré-requisitos

- .NET SDK 9.0, disponível no `PATH`: `dotnet --version` deve retornar `9.x`.
- Um navegador moderno com JavaScript habilitado.
- macOS, Linux ou Windows; não há serviços pagos, credenciais, banco externo ou runtime de terceiros.

## Executar

No diretório deste README:

```bash
dotnet restore
dotnet run
```

Abra a URL exibida pelo comando (por padrão, `http://localhost:5000` ou a porta informada pelo ASP.NET Core). Para iniciar em uma porta fixa:

```bash
dotnet run --urls http://localhost:5050
```

O progresso é salvo pela chave `trilha-csharp-dotnet-senior-progress` no armazenamento local do navegador. Ele não é enviado para servidor e pode ser reiniciado removendo essa chave nas ferramentas de desenvolvimento.

## Build e validação

```bash
dotnet build
dotnet test
```

Este artefato é um projeto Blazor executável e não adiciona um projeto de testes automatizados; por isso `dotnet test` valida o projeto sem descobrir testes. Os exemplos de teste na interface são material didático.

Para publicar um build local:

```bash
dotnet publish -c Release -o ./publish
dotnet ./publish/TrilhaCsharpDotnetSenior.dll
```

## Sequência de aprendizagem

1. **C# e o runtime** — tipos, memória, async/await, exceções e diagnóstico.
2. **Orientação a objetos e design** — invariantes, SOLID, composição e fronteiras.
3. **ASP.NET Core e Web APIs** — pipeline, contratos, validação e segurança web.
4. **Dados e persistência** — SQL, transações, idempotência, cache e migrações.
5. **Testes, qualidade e observabilidade** — testes no nível certo, sinais e entrega.
6. **Distribuídos, segurança, performance e liderança** — resiliência, threat modeling, budgets e decisões técnicas.
7. **Capstone** — plataforma de pedidos resiliente, com contrato, outbox, telemetria e ADR.

Cada módulo possui três aulas com objetivos e tarefas, além de um self-check. A conclusão é marcada na página do módulo e aparece no roadmap.

## Escopo e arquitetura

- Target framework: `net9.0` (ASP.NET Core Blazor Web App com render mode Interactive Server).
- Conteúdo estático e tipado em `Models/LearningModels.cs` para manter o material revisável e sem dependência de CMS.
- Páginas em `Components/Pages`, layout acessível em `Components/Layout` e estilos locais em `wwwroot/app.css`.
- A persistência é uma integração mínima de JavaScript em `wwwroot/js/progress.js`, limitada ao `localStorage` do navegador.
- Não há alteração de módulos de estudo existentes, site, workflows, configurações ou arquivos fora de `artifacts/csharp-dotnet-senior-path/`.
- O código-fonte e os comentários de código estão em inglês; o conteúdo apresentado ao aprendiz está em português brasileiro.

## Acessibilidade e responsividade

O layout usa landmarks semânticos, headings hierárquicos, labels para controles, estados `role="status"`/`role="progressbar"`, foco visível e contraste reforçado. O CSS adapta roadmap, aulas e self-check para telas menores sem depender de framework de UI.
