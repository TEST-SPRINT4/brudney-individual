import java.io.File

object Scripts {

    var Exe: List<Process> = listOf()

    fun executar() {
        val python1 = Runtime.getRuntime().exec("py main")
        val python2 = Runtime.getRuntime().exec("py main2")
        PythonExe = listOf(python1, python2)
    }

    fun parar() {
        for (processo in Exe) {
            processo.destroyForcibly()
        }
    }
}