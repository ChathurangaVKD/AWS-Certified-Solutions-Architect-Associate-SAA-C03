namespace TrilhaCsharpDotnetSenior.Models;

public sealed record CSharpSyntaxToken(string Text, string CssClass);

public static class CSharpSyntaxHighlighter
{
    private static readonly HashSet<string> Keywords = new(StringComparer.Ordinal)
    {
        "abstract", "as", "base", "bool", "break", "byte", "case", "catch", "char", "checked",
        "class", "const", "continue", "decimal", "default", "delegate", "do", "double", "else",
        "enum", "event", "explicit", "extern", "false", "finally", "fixed", "float", "for",
        "foreach", "goto", "if", "implicit", "in", "int", "interface", "internal", "is", "lock",
        "long", "namespace", "new", "null", "object", "operator", "out", "override", "params",
        "private", "protected", "public", "readonly", "record", "ref", "return", "sbyte", "sealed",
        "short", "sizeof", "stackalloc", "static", "string", "struct", "switch", "this", "throw",
        "true", "try", "typeof", "uint", "ulong", "unchecked", "unsafe", "ushort", "using", "var",
        "virtual", "void", "volatile", "while", "with", "async", "await", "yield"
    };

    private static readonly HashSet<string> Constants = new(StringComparer.Ordinal)
    {
        "false", "null", "true"
    };

    private static readonly HashSet<string> BuiltInTypes = new(StringComparer.Ordinal)
    {
        "bool", "byte", "char", "decimal", "double", "float", "int", "long", "object", "sbyte",
        "short", "string", "uint", "ulong", "ushort", "void"
    };

    private static readonly string[] Operators =
    [
        "??=", ">>>=", "<<=", ">>=", "=>", "??", "?.", "..", "++", "--", "&&", "||", "==", "!=",
        "<=", ">=", "+=", "-=", "*=", "/=", "%=", "<<", ">>", "&=", "|=", "^=", "+", "-", "*", "/",
        "%", "=", "!", "<", ">", "&", "|", "^", "~", "?"
    ];

    public static IReadOnlyList<CSharpSyntaxToken> Tokenize(string source)
    {
        ArgumentNullException.ThrowIfNull(source);

        var tokens = new List<CSharpSyntaxToken>();
        var index = 0;

        while (index < source.Length)
        {
            var start = index;
            var current = source[index];

            if (char.IsWhiteSpace(current))
            {
                index = ConsumeWhile(source, index, char.IsWhiteSpace);
                AddToken(tokens, source, start, index, "token-whitespace");
                continue;
            }

            if (current == '/' && index + 1 < source.Length && source[index + 1] == '/')
            {
                index = ConsumeUntilLineBreak(source, index);
                AddToken(tokens, source, start, index, "token-comment");
                continue;
            }

            if (current == '/' && index + 1 < source.Length && source[index + 1] == '*')
            {
                index = ConsumeBlockComment(source, index);
                AddToken(tokens, source, start, index, "token-comment");
                continue;
            }

            if (current == '#' && IsStartOfLine(source, index))
            {
                index = ConsumeUntilLineBreak(source, index);
                AddToken(tokens, source, start, index, "token-preprocessor");
                continue;
            }

            if (IsStringStart(source, index))
            {
                index = ConsumeString(source, index);
                AddToken(tokens, source, start, index, "token-string");
                continue;
            }

            if (current == '\'')
            {
                index = ConsumeCharacter(source, index);
                AddToken(tokens, source, start, index, "token-string");
                continue;
            }

            if (char.IsDigit(current))
            {
                index = ConsumeNumber(source, index);
                AddToken(tokens, source, start, index, "token-number");
                continue;
            }

            if (IsIdentifierStart(current))
            {
                index = ConsumeIdentifier(source, index);
                var identifier = source[start..index];
                AddToken(tokens, source, start, index, ClassifyIdentifier(source, start, index, identifier));
                continue;
            }

            var op = Operators.FirstOrDefault(value => source.AsSpan(index).StartsWith(value.AsSpan(), StringComparison.Ordinal));
            if (op is not null)
            {
                index += op.Length;
                AddToken(tokens, source, start, index, "token-operator");
                continue;
            }

            index++;
            AddToken(tokens, source, start, index, IsPunctuation(current) ? "token-punctuation" : "token-text");
        }

        return tokens;
    }

    private static string ClassifyIdentifier(string source, int start, int end, string identifier)
    {
        if (Constants.Contains(identifier))
            return "token-constant";

        if (Keywords.Contains(identifier))
            return BuiltInTypes.Contains(identifier) ? "token-type" : "token-keyword";

        var next = SkipWhitespace(source, end);
        if (next < source.Length && source[next] == '(')
            return "token-method";

        var previous = PreviousNonWhitespace(source, start);
        if (previous >= 0 && source[previous] == '.')
            return "token-property";

        return char.IsUpper(identifier[0]) ? "token-type" : "token-identifier";
    }

    private static bool IsStringStart(string source, int index)
    {
        var prefixLength = 0;
        while (index + prefixLength < source.Length && (source[index + prefixLength] is '@' or '$'))
            prefixLength++;

        return index + prefixLength < source.Length && source[index + prefixLength] == '"';
    }

    private static int ConsumeString(string source, int index)
    {
        var prefixEnd = index;
        while (prefixEnd < source.Length && (source[prefixEnd] is '@' or '$'))
            prefixEnd++;

        var isVerbatim = source[index..prefixEnd].Contains('@');
        var quoteStart = prefixEnd;
        var isRaw = quoteStart + 2 < source.Length && source[quoteStart..(quoteStart + 3)] == "\"\"\"";
        var quoteLength = isRaw ? 3 : 1;
        var cursor = quoteStart + quoteLength;

        while (cursor < source.Length)
        {
            if (isRaw)
            {
                if (cursor + 2 < source.Length && source[cursor..(cursor + 3)] == "\"\"\"")
                    return cursor + 3;

                cursor++;
                continue;
            }

            if (!isVerbatim && source[cursor] == '\\')
            {
                cursor += Math.Min(2, source.Length - cursor);
                continue;
            }

            if (source[cursor] == '"')
            {
                if (isVerbatim && cursor + 1 < source.Length && source[cursor + 1] == '"')
                {
                    cursor += 2;
                    continue;
                }

                return cursor + 1;
            }

            cursor++;
        }

        return source.Length;
    }

    private static int ConsumeCharacter(string source, int index)
    {
        var cursor = index + 1;
        while (cursor < source.Length)
        {
            if (source[cursor] == '\\')
            {
                cursor += Math.Min(2, source.Length - cursor);
                continue;
            }

            if (source[cursor] == '\'')
                return cursor + 1;

            cursor++;
        }

        return source.Length;
    }

    private static int ConsumeNumber(string source, int index)
    {
        var cursor = index;
        while (cursor < source.Length && (char.IsLetterOrDigit(source[cursor]) || source[cursor] is '_' or '.'))
            cursor++;

        return cursor;
    }

    private static int ConsumeIdentifier(string source, int index)
    {
        var cursor = index + 1;
        while (cursor < source.Length && IsIdentifierPart(source[cursor]))
            cursor++;

        return cursor;
    }

    private static int ConsumeWhile(string source, int index, Func<char, bool> predicate)
    {
        var cursor = index;
        while (cursor < source.Length && predicate(source[cursor]))
            cursor++;

        return cursor;
    }

    private static int ConsumeUntilLineBreak(string source, int index)
    {
        var cursor = index;
        while (cursor < source.Length && source[cursor] is not '\r' and not '\n')
            cursor++;

        return cursor;
    }

    private static int ConsumeBlockComment(string source, int index)
    {
        var end = source.IndexOf("*/", index + 2, StringComparison.Ordinal);
        return end < 0 ? source.Length : end + 2;
    }

    private static int SkipWhitespace(string source, int index)
    {
        while (index < source.Length && char.IsWhiteSpace(source[index]))
            index++;

        return index;
    }

    private static int PreviousNonWhitespace(string source, int index)
    {
        var cursor = index - 1;
        while (cursor >= 0 && char.IsWhiteSpace(source[cursor]))
            cursor--;

        return cursor;
    }

    private static bool IsStartOfLine(string source, int index) =>
        source[..index].All(character => character is '\r' or '\n' or ' ' or '\t');

    private static bool IsIdentifierStart(char character) => character == '_' || char.IsLetter(character);

    private static bool IsIdentifierPart(char character) => character == '_' || char.IsLetterOrDigit(character);

    private static bool IsPunctuation(char character) => "{}[]();,.:".Contains(character);

    private static void AddToken(ICollection<CSharpSyntaxToken> tokens, string source, int start, int end, string cssClass) =>
        tokens.Add(new CSharpSyntaxToken(source[start..end], $"token {cssClass}"));
}
