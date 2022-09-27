#version 330 core
out vec4 FragColor;
in vec2 TexCoords;

uniform sampler2D texture_diffuse0;

void main()
{
    vec4 texColor = texture(texture_diffuse0, TexCoords);
    if(texColor.a < 0.1){
        discard;
    }
    FragColor = vec4(vec3(texColor), 1.0);
}