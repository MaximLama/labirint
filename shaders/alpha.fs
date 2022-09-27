#version 330 core
out vec4 FragColor;
in vec2 TexCoords;

uniform sampler2D texture_diffuse0;

void main()
{
    //vec3 diffuse = material.diffuse_color * vec3(1, 1, 1);
    //vec3 ambient = material.ambient_color * vec3(0.2, 0.2, 0.2);
    //vec3 result = (ambient + diffuse) * vec3(texture(material.texture_diffuse0, TexCoords));
    vec4 texColor = texture(texture_diffuse0, TexCoords);
    if(texColor.r + texColor.g + texColor.b < 0.1 ){
        discard;
    }
    FragColor = texColor;
}